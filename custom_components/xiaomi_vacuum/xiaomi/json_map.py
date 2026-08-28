"""Map support for Xiaomi-branded vacuums that serve a JSON map.

These models (xiaomi.vacuum.d109gl and relatives) do not use Dreame's binary
frame format. They upload a small JSON envelope to the Xiaomi file service:

    {"version": 2, "data": "<base64 AES-CBC ciphertext>"}

which decrypts to a zlib-compressed JSON document describing the whole map.

The AES key is not a secret and does not need a keystore entry: the device's
own Mi Home plugin derives it from the model string and the device id, so it can
be reproduced for any device of a supported model. Recovered from the plugin
bundle (`files/plugin/install/rn/<pid>/<vid>/android/main.bundle`):

    MODEL_KEY   = Device.model.slice(-16)
    IV          = "ABCDEF1234123412"
    ENC_KEY     = AES-CBC(MODEL_KEY + deviceId, key=MODEL_KEY, iv=IV, Pkcs7)
    DECRYPT_KEY = MD5(ENC_KEY)            # 16 raw bytes, AES-128
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import zlib
from typing import Any

_LOGGER = logging.getLogger(__name__)

MAP_IV: bytes = b"ABCDEF1234123412"

# Wall/void markers in the occupancy grid. Every other non-zero value is a room
# id and matches the ids in map_room_info / room_attrs.
GRID_EMPTY = 0
GRID_WALL = 255

WALL_COLOR = (70, 80, 95, 255)
FLOOR_COLOR = (226, 232, 240, 255)
ROOM_COLORS = [
    (122, 183, 240), (160, 215, 145), (245, 205, 120), (230, 150, 165),
    (180, 165, 220), (140, 210, 205), (240, 175, 130), (200, 200, 160),
    (170, 190, 230), (215, 180, 150), (150, 195, 175), (225, 195, 215),
]
ROUTE_COLOR = (255, 255, 255, 235)
ROUTE_WIDTH = 3
SCALE = 4


def derive_key(model: str, device_id: Any) -> bytes:
    """Reproduce the plugin's map key for this model and device."""
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    model_key = model[-16:].encode()
    original = model_key + str(device_id).encode()
    padding = 16 - (len(original) % 16)
    padded = original + bytes([padding]) * padding
    encryptor = Cipher(
        algorithms.AES(model_key), modes.CBC(MAP_IV), backend=default_backend()
    ).encryptor()
    enc_key = encryptor.update(padded) + encryptor.finalize()
    return bytes.fromhex(hashlib.md5(enc_key).hexdigest())


def decrypt_map(raw: bytes, key: bytes) -> dict[str, Any] | None:
    """Turn a downloaded map object into the decoded map document."""
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    try:
        envelope = json.loads(raw)
        data = envelope["data"].replace("_", "/").replace("-", "+")
        blob = base64.b64decode(data)
        decryptor = Cipher(
            algorithms.AES(key), modes.CBC(MAP_IV), backend=default_backend()
        ).decryptor()
        plain = decryptor.update(blob) + decryptor.finalize()
        if plain and 0 < plain[-1] <= 16:
            plain = plain[: -plain[-1]]
        return json.loads(zlib.decompress(plain))
    except Exception as ex:  # noqa: BLE001 - never let a bad frame kill the poll
        _LOGGER.debug("JSON map decode failed: %s", ex)
        return None


def map_label(map_data: dict[str, Any]) -> str:
    """A stable, human name for this map.

    Used as the camera's state. It must not be a timestamp: the map object is
    re-fetched on every poll while cleaning, and a timestamp state turns the
    logbook into a wall of meaningless entries.
    """
    name = (map_data.get("map_name") or "").strip()
    if name:
        return name
    map_id = map_data.get("map_id")
    return f"Map {map_id}" if map_id is not None else "Map"


def room_names(map_data: dict[str, Any]) -> dict[int, str]:
    """Room id -> name, for the rooms the device knows about."""
    names: dict[int, str] = {}
    for room in map_data.get("room_attrs") or []:
        room_id = room.get("id")
        if room_id is not None:
            names[int(room_id)] = room.get("room_name") or f"Room {room_id}"
    return names


def render_map(map_data: dict[str, Any]) -> bytes | None:
    """Render the map document to a PNG."""
    from PIL import Image, ImageDraw

    try:
        width = int(map_data["width"])
        height = int(map_data["height"])
        grid = zlib.decompress(base64.b64decode(map_data["map_data"]))
        if len(grid) < width * height:
            _LOGGER.debug("Map grid too short: %s < %s", len(grid), width * height)
            return None

        room_ids = sorted({int(r["room_id"]) for r in map_data.get("map_room_info") or []})
        colors = {rid: ROOM_COLORS[i % len(ROOM_COLORS)] for i, rid in enumerate(room_ids)}

        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        pixels = image.load()
        for y in range(height):
            offset = y * width
            for x in range(width):
                value = grid[offset + x]
                if value == GRID_EMPTY:
                    continue
                if value == GRID_WALL:
                    pixels[x, y] = WALL_COLOR
                elif value in colors:
                    pixels[x, y] = (*colors[value], 255)
                else:
                    pixels[x, y] = FLOOR_COLOR

        image = image.resize((width * SCALE, height * SCALE), Image.NEAREST)
        draw = ImageDraw.Draw(image)
        resolution = int(map_data.get("resolution") or 0)

        if map_data.get("have_pile"):
            px = int(map_data.get("pile_x", 0)) * SCALE
            py = int(map_data.get("pile_y", 0)) * SCALE
            draw.ellipse([px - 11, py - 11, px + 11, py + 11], fill=(35, 45, 60, 255))
            draw.ellipse([px - 5, py - 5, px + 5, py + 5], fill=(250, 250, 250, 255))

        # Cleaning route the robot actually drove, in world mm like position.
        paths = (map_data.get("paths") or {}).get("points") or []
        if paths and resolution:
            route = [
                (
                    (int(pt["x"]) - int(map_data["origin_x"])) / resolution * SCALE,
                    (int(pt["y"]) - int(map_data["origin_y"])) / resolution * SCALE,
                )
                for pt in paths
                if "x" in pt and "y" in pt
            ]
            if len(route) > 1:
                draw.line(route, fill=ROUTE_COLOR, width=ROUTE_WIDTH, joint="curve")

        position = map_data.get("position") or {}
        if position and resolution:
            rx = (int(position["x"]) - int(map_data["origin_x"])) / resolution * SCALE
            ry = (int(position["y"]) - int(map_data["origin_y"])) / resolution * SCALE
            draw.ellipse([rx - 13, ry - 13, rx + 13, ry + 13], fill=(255, 255, 255, 255))
            draw.ellipse([rx - 9, ry - 9, rx + 9, ry + 9], fill=(52, 120, 246, 255))

        # Device grid origin is bottom-left; images are drawn top-left.
        image = image.transpose(Image.FLIP_TOP_BOTTOM)

        from io import BytesIO

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return buffer.getvalue()
    except Exception as ex:  # noqa: BLE001
        _LOGGER.debug("JSON map render failed: %s", ex)
        return None

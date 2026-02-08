# Xiaomi Vacuum integration for Home Assistant

Home Assistant custom integration for Xiaomi robot vacuums using the MIoT protocol.

Forked from [Tasshack/dreame-vacuum](https://github.com/Tasshack/dreame-vacuum) — rebranded and refocused for Xiaomi-branded devices.

## Supported Devices

- `xiaomi.vacuum.d109gl` *(Xiaomi X20 Max)*

## Features

- Auto generated device entities
- Live and multi floor map support
- Customized room cleaning entities
- [Services for device and map with examples](docs/services.md)
- [Persistent notifications and error reporting](docs/notifications.md)
- [Events for automations](docs/events.md)

## Installation

### Via [HACS](https://hacs.xyz/)

Add this repository as a custom repository in HACS:
1. Open HACS in Home Assistant
2. Click the three dots menu → Custom repositories
3. Add `https://github.com/voska/dreame-vacuum` with category "Integration"
4. Install **Xiaomi Vacuum**

### Manually

```sh
wget -O - https://raw.githubusercontent.com/voska/dreame-vacuum/master/install | bash -
```

## Configuration

1. Add the **Xiaomi Vacuum** integration in Settings → Devices & Services → Add Integration
2. Select **Xiaomi Vacuum** from the list
3. Select configuration type and enter credentials
4. Set your device name and integration settings

## How to Use

Integration is compatible with all available Lovelace vacuum cards.

#### With [Xiaomi Vacuum Map Card](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card)

```yaml
type: custom:xiaomi-vacuum-map-card
entity: # Your vacuum entity
map_source:
  camera: # Map Entity
calibration_source:
  camera: true
vacuum_platform: voska/dreame-vacuum
```

#### With [Vacuum Card](https://github.com/denysdovhan/vacuum-card)

```yaml
type: custom:vacuum-card
entity: # Your vacuum entity
map: # Map Entity
map_refresh: 1
stats:
  default:
    - attribute: filter_left
      unit: '%'
      subtitle: Filter
    - attribute: side_brush_left
      unit: '%'
      subtitle: Side brush
    - attribute: main_brush_left
      unit: '%'
      subtitle: Main brush
    - attribute: sensor_dirty_left
      unit: '%'
      subtitle: Sensors
  cleaning:
    - attribute: cleaned_area
      unit: m²
      subtitle: Cleaned area
    - attribute: cleaning_time
      unit: min
      subtitle: Cleaning time
shortcuts:
  - name: Clean Room 1
    service: xiaomi_vacuum.vacuum_clean_segment
    service_data:
      entity_id: # Your vacuum entity
      segments: 1
    icon: mdi:sofa
```

## Thanks To

 - [Tasshack/dreame-vacuum](https://github.com/Tasshack/dreame-vacuum) — original integration
 - [xiaomi_vacuum](https://github.com/pooyashahidi/xiaomi_vacuum) by [@pooyashahidi](https://github.com/pooyashahidi)
 - [Xiaomi MIoT for Home Assistant](https://github.com/ha0y/xiaomi_miot_raw) by [@ha0y](https://github.com/ha0y)
 - [Xiaomi Cloud Map Extractor](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor) by [@PiotrMachowski](https://github.com/PiotrMachowski)

from typing import Final
from .types import (
    XiaomiVacuumChargingStatus,
    XiaomiVacuumTaskStatus,
    XiaomiVacuumState,
    XiaomiVacuumWaterTank,
    XiaomiVacuumCarpetSensitivity,
    XiaomiVacuumStatus,
    XiaomiVacuumErrorCode,
    XiaomiVacuumRelocationStatus,
    XiaomiVacuumDustCollection,
    XiaomiVacuumAutoEmptyStatus,
    XiaomiVacuumSelfWashBaseStatus,
    XiaomiVacuumSuctionLevel,
    XiaomiVacuumWaterVolume,
    XiaomiVacuumMopPadHumidity,
    XiaomiVacuumCleaningMode,
    XiaomiVacuumSelfCleanArea,
    XiaomiVacuumMopWashLevel,
    XiaomiVacuumMoppingType,
    XiaomiVacuumProperty,
    XiaomiVacuumAction,
)

SUCTION_LEVEL_QUIET: Final = "quiet"
SUCTION_LEVEL_STANDARD: Final = "standard"
SUCTION_LEVEL_STRONG: Final = "strong"
SUCTION_LEVEL_TURBO: Final = "turbo"

WATER_VOLUME_LOW: Final = "low"
WATER_VOLUME_MEDIUM: Final = "medium"
WATER_VOLUME_HIGH: Final = "high"

MOP_PAD_HUMIDITY_SLIGHTLY_DRY: Final = "slightly_dry"
MOP_PAD_HUMIDITY_MOIST: Final = "moist"
MOP_PAD_HUMIDITY_WET: Final = "wet"

CLEANING_MODE_SWEEPING: Final = "sweeping"
CLEANING_MODE_MOPPING: Final = "mopping"
CLEANING_MODE_SWEEPING_AND_MOPPING: Final = "sweeping_and_mopping"

STATE_UNKNOWN: Final = "unknown"
STATE_SWEEPING: Final = "sweeping"
STATE_IDLE: Final = "idle"
STATE_PAUSED: Final = "paused"
STATE_RETURNING: Final = "returning"
STATE_CHARGING: Final = "charging"
STATE_ERROR: Final = "error"
STATE_MOPPING: Final = "mopping"
STATE_DRYING: Final = "drying"
STATE_WASHING: Final = "washing"
STATE_RETURNING_WASHING: Final = "returning_to_washing"
STATE_BUILDING: Final = "building"
STATE_SWEEPING_AND_MOPPING: Final = "sweeping_and_mopping"
STATE_CHARGING_COMPLETED: Final = "charging_completed"
STATE_UPGRADING: Final = "upgrading"
STATE_UNAVAILABLE: Final = "unavailable"
STATE_CLEANING: Final = "cleaning"
STATE_DOCKED: Final = "docked"

TASK_STATUS_COMPLETED: Final = "completed"
TASK_STATUS_AUTO_CLEANING: Final = "cleaning"
TASK_STATUS_ZONE_CLEANING: Final = "zone_cleaning"
TASK_STATUS_SEGMENT_CLEANING: Final = "room_cleaning"
TASK_STATUS_SPOT_CLEANING: Final = "spot_cleaning"
TASK_STATUS_FAST_MAPPING: Final = "fast_mapping"
TASK_STATUS_AUTO_CLEANING_PAUSE: Final = "cleaning_paused"
TASK_STATUS_SEGMENT_CLEANING_PAUSE: Final = "room_cleaning_paused"
TASK_STATUS_ZONE_CLEANING_PAUSE: Final = "zone_cleaning_paused"
TASK_STATUS_SPOT_CLEANING_PAUSE: Final = "spot_cleaning_paused"
TASK_STATUS_MAP_CLEANING_PAUSE: Final = "map_cleaning_paused"
TASK_STATUS_DOCKING_PAUSE: Final = "docking_paused"
TASK_STATUS_MOPPING_PAUSE: Final = "mopping_paused"
TASK_STATUS_ZONE_MOPPING_PAUSE: Final = "zone_mopping_paused"
TASK_STATUS_SEGMENT_MOPPING_PAUSE: Final = "room_mopping_paused"
TASK_STATUS_AUTO_MOPPING_PAUSE: Final = "mopping_paused"
TASK_STATUS_MONITOR_CRUISE: Final = "monitor_cruise"
TASK_STATUS_MONITOR_CRUISE_PAUSE: Final = "monitor_cruise_pause"
TASK_STATUS_MONITOR_SPOT: Final = "monitor_spot"
TASK_STATUS_MONITOR_SPOT_PAUSE: Final = "monitor_spot_pause"
TASK_STATUS_SUMMON_CLEAN_PAUSE: Final = "summon_clean_pause"
TASK_STATUS_RETURNING_INSTALL_MOP: Final = "returning_to_install_mop"
TASK_STATUS_RETURNING_REMOVE_MOP: Final = "returning_to_remove_mop"

STATUS_CLEANING: Final = "cleaning"
STATUS_FOLLOW_WALL: Final = "follow_wall_cleaning"
STATUS_CHARGING: Final = "charging"
STATUS_OTA: Final = "ota"
STATUS_FCT: Final = "fct"
STATUS_WIFI_SET: Final = "wifi_set"
STATUS_POWER_OFF: Final = "power_off"
STATUS_FACTORY: Final = "factory"
STATUS_ERROR: Final = "error"
STATUS_REMOTE_CONTROL: Final = "remote_control"
STATUS_SLEEP: Final = "sleeping"
STATUS_SELF_TEST: Final = "self_test"
STATUS_FACTORY_FUNC_TEST: Final = "factory_test"
STATUS_STANDBY: Final = "standby"
STATUS_SEGMENT_CLEANING: Final = "room_cleaning"
STATUS_ZONE_CLEANING: Final = "zone_cleaning"
STATUS_SPOT_CLEANING: Final = "spot_cleaning"
STATUS_FAST_MAPPING: Final = "fast_mapping"
STATUS_MONITOR_CRUISE: Final = "monitor_cruise"
STATUS_MONITOR_SPOT: Final = "monitor_spot"
STATUS_SUMMON_CLEAN: Final = "summon_clean"

RELOCATION_STATUS_LOCATED: Final = "located"
RELOCATION_STATUS_LOCATING: Final = "locating"
RELOCATION_STATUS_FAILED: Final = "failed"
RELOCATION_STATUS_SUCESS: Final = "success"

CHARGING_STATUS_CHARGING: Final = "charging"
CHARGING_STATUS_NOT_CHARGING: Final = "not_charging"
CHARGING_STATUS_RETURN_TO_CHARGE: Final = "return_to_charge"
CHARGING_STATUS_CHARGING_COMPLETED: Final = "charging_completed"

DUST_COLLECTION_NOT_AVAILABLE: Final = "not_available"
DUST_COLLECTION_AVAILABLE: Final = "available"

AUTO_EMPTY_STATUS_ACTIVE: Final = "active"
AUTO_EMPTY_STATUS_NOT_PERFORMED: Final = "not_performed"

SELF_WASH_BASE_STATUS_WASHING: Final = "washing"
SELF_WASH_BASE_STATUS_DRYING: Final = "drying"
SELF_WASH_BASE_STATUS_PAUSED: Final = "paused"
SELF_WASH_BASE_STATUS_RETURNING: Final = "returning"
SELF_WASH_BASE_STATUS_CLEAN_ADD_WATER: Final = "clean_add_water"
SELF_WASH_BASE_STATUS_ADDING_WATER: Final = "adding_water"

SELF_AREA_CLEAN_FIVE_SQUARE_METERS: Final = "five_square_meters"
SELF_AREA_CLEAN_TEN_SQUARE_METERS: Final = "ten_square_meters"
SELF_AREA_CLEAN_FIFTEEN_SQUARE_METERS: Final = "fifteen_square_meters"
SELF_AREA_CLEAN_SINGLE_ZONE: Final = "single_zone"

MOP_WASH_LEVEL_DEEP: Final = "deep"
MOP_WASH_LEVEL_DAILY: Final = "daily"
MOP_WASH_LEVEL_WATER_SAVING: Final = "water_saving"

MOPPING_TYPE_DEEP: Final = "deep"
MOPPING_TYPE_DAILY: Final = "daily"
MOPPING_TYPE_ACCURATE: Final = "accurate"

WATER_TANK_INSTALLED: Final = "installed"
WATER_TANK_NOT_INSTALLED: Final = "not_installed"
WATER_TANK_MOP_INSTALLED: Final = "mop_installed"

CARPET_SENSITIVITY_LOW: Final = "low"
CARPET_SENSITIVITY_MEDIUM: Final = "medium"
CARPET_SENSITIVITY_HIGH: Final = "high"

ERROR_NO_ERROR: Final = "no_error"
ERROR_DROP: Final = "drop"
ERROR_CLIFF: Final = "cliff"
ERROR_BUMPER: Final = "bumper"
ERROR_GESTURE: Final = "gesture"
ERROR_BUMPER_REPEAT: Final = "bumper_repeat"
ERROR_DROP_REPEAT: Final = "drop_repeat"
ERROR_OPTICAL_FLOW: Final = "optical_flow"
ERROR_NO_BOX: Final = "no_box"
ERROR_NO_TANKBOX: Final = "no_tank_box"
ERROR_WATERBOX_EMPTY: Final = "water_box_empty"
ERROR_BOX_FULL: Final = "box_full"
ERROR_BRUSH: Final = "brush"
ERROR_SIDE_BRUSH: Final = "side_brush"
ERROR_FAN: Final = "fan"
ERROR_LEFT_WHEEL_MOTOR: Final = "left_wheel_motor"
ERROR_RIGHT_WHEEL_MOTOR: Final = "right_wheel_motor"
ERROR_TURN_SUFFOCATE: Final = "turn_suffocate"
ERROR_FORWARD_SUFFOCATE: Final = "forward_suffocate"
ERROR_CHARGER_GET: Final = "charger_get"
ERROR_BATTERY_LOW: Final = "battery_low"
ERROR_CHARGE_FAULT: Final = "charge_fault"
ERROR_BATTERY_PERCENTAGE: Final = "battery_percentage"
ERROR_HEART: Final = "heart"
ERROR_CAMERA_OCCLUSION: Final = "camera_occlusion"
ERROR_MOVE: Final = "move"
ERROR_FLOW_SHIELDING: Final = "flow_shielding"
ERROR_INFRARED_SHIELDING: Final = "infrared_shielding"
ERROR_CHARGE_NO_ELECTRIC: Final = "charge_no_electric"
ERROR_BATTERY_FAULT: Final = "battery_fault"
ERROR_FAN_SPEED_ERROR: Final = "fan_speed_error"
ERROR_LEFTWHELL_SPEED: Final = "left_wheell_speed"
ERROR_RIGHTWHELL_SPEED: Final = "right_wheell_speed"
ERROR_BMI055_ACCE: Final = "bmi055_acce"
ERROR_BMI055_GYRO: Final = "bmi055_gyro"
ERROR_XV7001: Final = "xv7001"
ERROR_LEFT_MAGNET: Final = "left_magnet"
ERROR_RIGHT_MAGNET: Final = "right_magnet"
ERROR_FLOW_ERROR: Final = "flow_error"
ERROR_INFRARED_FAULT: Final = "infrared_fault"
ERROR_CAMERA_FAULT: Final = "camera_fault"
ERROR_STRONG_MAGNET: Final = "strong_magnet"
ERROR_WATER_PUMP: Final = "water_pump"
ERROR_RTC: Final = "rtc"
ERROR_AUTO_KEY_TRIG: Final = "auto_key_trig"
ERROR_P3V3: Final = "p3v3"
ERROR_CAMERA_IDLE: Final = "camera_idle"
ERROR_BLOCKED: Final = "blocked"
ERROR_LDS_ERROR: Final = "lds_error"
ERROR_LDS_BUMPER: Final = "lds_bumper"
ERROR_FILTER_BLOCKED: Final = "filter_blocked"
ERROR_EDGE: Final = "edge"
ERROR_CARPET: Final = "carpet"
ERROR_LASER: Final = "laser"
ERROR_ULTRASONIC: Final = "ultrasonic"
ERROR_NO_GO_ZONE: Final = "no_go_zone"
ERROR_ROUTE: Final = "route"
ERROR_RESTRICTED: Final = "restricted"
ERROR_REMOVE_MOP: Final = "remove_mop"
ERROR_MOP_REMOVED: Final = "mop_removed"
ERROR_MOP_PAD_STOP_ROTATE: Final = "mop_pad_stop_rotate"
ERROR_BIN_FULL: Final = "bin_full"
ERROR_BIN_OPEN: Final = "bin_open"
ERROR_WATER_TANK: Final = "water_tank"
ERROR_DIRTY_WATER_TANK: Final = "dirty_water_tank"
ERROR_WATER_TANK_DRY: Final = "water_tank_dry"
ERROR_DIRTY_WATER_TANK_BLOCKED: Final = "dirty_water_tank_blocked"
ERROR_DIRTY_WATER_TANK_PUMP: Final = "dirty_water_tank_pump"
ERROR_MOP_PAD: Final = "mop_pad"
ERROR_WET_MOP_PAD: Final = "wet_mop_pad"
ERROR_CLEAN_MOP_PAD: Final = "clean_mop_pad"
ERROR_CLEAN_TANK_LEVEL: Final = "clean_tank_level"
ERROR_DIRTY_TANK_LEVEL: Final = "dirty_tank_level"
ERROR_WASHBOARD_LEVEL: Final = "washboard_level"

ATTR_CHARGING: Final = "charging"
ATTR_STARTED: Final = "started"
ATTR_PAUSED: Final = "paused"
ATTR_RUNNING: Final = "running"
ATTR_RETURNING_PAUSED: Final = "returning_paused"
ATTR_RETURNING: Final = "returning"
ATTR_MAPPING: Final = "mapping"
ATTR_ROOMS: Final = "rooms"
ATTR_CURRENT_SEGMENT: Final = "current_segment"
ATTR_SELECTED_MAP: Final = "selected_map"
ATTR_ID: Final = "id"
ATTR_NAME: Final = "name"
ATTR_ICON: Final = "icon"
ATTR_STATUS: Final = "status"
ATTR_CLEANING_MODE: Final = "cleaning_mode"
ATTR_SUCTION_LEVEL: Final = "suction_level"
ATTR_WATER_TANK: Final = "water_tank"
ATTR_COMPLETED: Final = "completed"
ATTR_CLEANING_TIME: Final = "cleaning_time"
ATTR_CLEANED_AREA: Final = "cleaned_area"
ATTR_MOP_PAD_HUMIDITY: Final = "mop_pad_humidity"
ATTR_MOP_PAD: Final = "mop_pad"
ATTR_CLEANING_SEQUENCE: Final = "cleaning_sequence"

AI_SETTING_SWITCH: Final = "obstacle_detect_switch"
AI_SETTING_UPLOAD: Final = "obstacle_app_display_switch"
AI_SETTING_PET: Final = "whether_have_pet"
AI_SETTING_HUMAN: Final = "human_detect_switch"
AI_SETTING_FURNITURE: Final = "furniture_detect_switch"
AI_SETTING_FLUID: Final = "fluid_detect_switch"

MAP_PARAMETER_NAME: Final = "name"
MAP_PARAMETER_VALUE: Final = "value"
MAP_PARAMETER_TIME: Final = "time"
MAP_PARAMETER_CODE: Final = "code"
MAP_PARAMETER_OUT: Final = "out"
MAP_PARAMETER_MAP: Final = "map"
MAP_PARAMETER_ANGLE: Final = "angle"
MAP_PARAMETER_MAPSTR: Final = "mapstr"
MAP_PARAMETER_CURR_ID: Final = "curr_id"
MAP_PARAMETER_VACUUM: Final = "vacuum"
MAP_PARAMETER_ID: Final = "id"
MAP_PARAMETER_INFO: Final = "info"
MAP_PARAMETER_FIRST: Final = "first"
MAP_PARAMETER_OBJNAME: Final = "objname"
MAP_PARAMETER_RESULT: Final = "result"
MAP_PARAMETER_URL: Final = "url"
MAP_PARAMETER_EXPIRES_TIME: Final = "expires_time"
MAP_PARAMETER_THB: Final = "thb"
MAP_PARAMETER_OBJECT_NAME: Final = "object_name"
MAP_PARAMETER_MD5: Final = "md5"

MAP_REQUEST_PARAMETER_MAP_ID: Final = "map_id"
MAP_REQUEST_PARAMETER_FRAME_ID: Final = "frame_id"
MAP_REQUEST_PARAMETER_FRAME_TYPE: Final = "frame_type"
MAP_REQUEST_PARAMETER_REQ_TYPE: Final = "req_type"
MAP_REQUEST_PARAMETER_FORCE_TYPE: Final = "force_type"
MAP_REQUEST_PARAMETER_TYPE: Final = "type"
MAP_REQUEST_PARAMETER_INDEX: Final = "index"
MAP_REQUEST_PARAMETER_ROOM_ID: Final = "roomID"

MAP_DATA_PARAMETER_CLASS: Final = "__class"
MAP_DATA_PARAMETER_SIZE: Final = "size"
MAP_DATA_PARAMETER_X: Final = "x"
MAP_DATA_PARAMETER_Y: Final = "y"
MAP_DATA_PARAMETER_PIXEL_SIZE: Final = "pixelSize"
MAP_DATA_PARAMETER_LAYERS: Final = "layers"
MAP_DATA_PARAMETER_ENTITIES: Final = "entities"
MAP_DATA_PARAMETER_META_DATA: Final = "metaData"
MAP_DATA_PARAMETER_VERSION: Final = "version"
MAP_DATA_PARAMETER_ROTATION: Final = "rotation"
MAP_DATA_PARAMETER_TYPE: Final = "type"
MAP_DATA_PARAMETER_POINTS: Final = "points"
MAP_DATA_PARAMETER_PIXELS: Final = "pixels"
MAP_DATA_PARAMETER_SEGMENT_ID: Final = "segmentId"
MAP_DATA_PARAMETER_ACTIVE: Final = "active"
MAP_DATA_PARAMETER_NAME: Final = "name"
MAP_DATA_PARAMETER_DIMENSIONS: Final = "dimensions"
MAP_DATA_PARAMETER_MIN: Final = "min"
MAP_DATA_PARAMETER_MAX: Final = "max"
MAP_DATA_PARAMETER_MID: Final = "mid"
MAP_DATA_PARAMETER_AVG: Final = "avg"
MAP_DATA_PARAMETER_PIXEL_COUNT: Final = "pixelCount"
MAP_DATA_PARAMETER_COMPRESSED_PIXELS: Final = "compressedPixels"
MAP_DATA_PARAMETER_ROBOT_POSITION: Final = "robot_position"
MAP_DATA_PARAMETER_CHARGER_POSITION: Final = "charger_location"
MAP_DATA_PARAMETER_NO_MOP_AREA: Final = "no_mop_area"
MAP_DATA_PARAMETER_NO_GO_AREA: Final = "no_go_area"
MAP_DATA_PARAMETER_ACTIVE_ZONE: Final = "active_zone"
MAP_DATA_PARAMETER_VIRTUAL_WALL: Final = "virtual_wall"
MAP_DATA_PARAMETER_PATH: Final = "path"
MAP_DATA_PARAMETER_FLOOR: Final = "floor"
MAP_DATA_PARAMETER_WALL: Final = "wall"
MAP_DATA_PARAMETER_SEGMENT: Final = "segment"

PROPERTY_TO_NAME: Final = {
    XiaomiVacuumProperty.STATE: ["state", "State"],
    XiaomiVacuumProperty.ERROR: ["error", "Error"],
    XiaomiVacuumProperty.BATTERY_LEVEL: ["battery_level", "Battery Level"],
    XiaomiVacuumProperty.CHARGING_STATUS: ["charging_status", "Charging Status"],
    XiaomiVacuumProperty.STATUS: ["status", "Status"],
    XiaomiVacuumProperty.CLEANING_TIME: ["cleaning_time", "Cleaning Time"],
    XiaomiVacuumProperty.CLEANED_AREA: ["cleaned_area", "Cleaned Area"],
    XiaomiVacuumProperty.SUCTION_LEVEL: ["suction_level", "Suction Level"],
    XiaomiVacuumProperty.WATER_VOLUME: ["water_volume", "Water Volume"],
    XiaomiVacuumProperty.WATER_TANK: ["water_tank", "Water Tank"],
    XiaomiVacuumProperty.TASK_STATUS: ["task_status", "Task Status"],
    XiaomiVacuumProperty.RESUME_CLEANING: ["resume_cleaning", "Resume Cleaning"],
    XiaomiVacuumProperty.CARPET_BOOST: ["carpet_boost", "Carpet Boost"],
    XiaomiVacuumProperty.REMOTE_CONTROL: ["remote_control", "Remote Control"],
    XiaomiVacuumProperty.MOP_CLEANING_REMAINDER: [
        "mop_cleaning_remainder",
        "Mop Cleaning Remainder",
    ],
    XiaomiVacuumProperty.CLEANING_PAUSED: ["cleaning_paused", "Cleaning Paused"],
    XiaomiVacuumProperty.FAULTS: ["faults", "Faults"],
    XiaomiVacuumProperty.RELOCATION_STATUS: ["relocation_status", "Relocation Status"],
    XiaomiVacuumProperty.OBSTACLE_AVOIDANCE: [
        "obstacle_avoidance",
        "Obstacle Avoidance",
    ],
    XiaomiVacuumProperty.AI_DETECTION: [
        "ai_obstacle_detection",
        "AI Obstacle Detection",
    ],
    XiaomiVacuumProperty.CLEANING_MODE: ["cleaning_mode", "Cleaning Mode"],
    XiaomiVacuumProperty.SELF_WASH_BASE_STATUS: [
        "self_wash_base_status",
        "Self-Wash Base Status",
    ],
    XiaomiVacuumProperty.CUSTOMIZED_CLEANING: [
        "customized_cleaning",
        "Customized Cleaning",
    ],
    XiaomiVacuumProperty.CHILD_LOCK: ["child_lock", "Child Lock"],
    XiaomiVacuumProperty.CARPET_SENSITIVITY: [
        "carpet_sensitivity",
        "Carpet Sensitivity",
    ],
    XiaomiVacuumProperty.TIGHT_MOPPING: ["tight_mopping", "Tight Mopping"],
    XiaomiVacuumProperty.CLEANING_CANCEL: ["cleaning_cancel", "Cleaning Cancel"],
    XiaomiVacuumProperty.CARPET_RECOGNITION: [
        "carpet_recognition",
        "Carpet Recognition",
    ],
    XiaomiVacuumProperty.SELF_CLEAN: ["self_clean", "Self-Clean"],
    XiaomiVacuumProperty.WARN_STATUS: ["warn_status", "Warn Status"],
    XiaomiVacuumProperty.CARPET_AVOIDANCE: ["carpet_avoidance", "Carpet Avoidance"],
    XiaomiVacuumProperty.AUTO_ADD_DETERGENT: [
        "auto_add_detergent",
        "Auto-Add Detergent",
    ],
    XiaomiVacuumProperty.DRYING_TIME: ["drying_time", "Drying Time"],
    XiaomiVacuumProperty.DND: ["dnd", "DnD"],
    XiaomiVacuumProperty.DND_START: ["dnd_start", "DnD Start"],
    XiaomiVacuumProperty.DND_END: ["dnd_end", "DnD End"],
    XiaomiVacuumProperty.MULTI_FLOOR_MAP: ["multi_floor_map", "Multi Floor Map"],
    XiaomiVacuumProperty.MAP_LIST: ["map_list", "Map List"],
    XiaomiVacuumProperty.RECOVERY_MAP_LIST: ["recovery_map_list", "Recovery Map List"],
    XiaomiVacuumProperty.MAP_RECOVERY: ["map_recovery", "Map Recovery"],
    XiaomiVacuumProperty.MAP_RECOVERY_STATUS: [
        "map_recovery_status",
        "Map Recovery Status",
    ],
    XiaomiVacuumProperty.VOLUME: ["volume", "Volume"],
    XiaomiVacuumProperty.SCHEDULE: ["schedule", "Schedule"],
    XiaomiVacuumProperty.AUTO_DUST_COLLECTING: [
        "auto_dust_collecting",
        "Auto Dust Collecting",
    ],
    XiaomiVacuumProperty.AUTO_EMPTY_FREQUENCY: [
        "auto_empty_frequency",
        "Auto Empty Frequency",
    ],
    XiaomiVacuumProperty.MAP_SAVING: [
        "map_saving",
        "Map Saving",
    ],
    XiaomiVacuumProperty.DUST_COLLECTION: ["dust_collection", "Dust Collection"],
    XiaomiVacuumProperty.AUTO_EMPTY_STATUS: ["auto_empty_status", "Auto Empty Status"],
    XiaomiVacuumProperty.SERIAL_NUMBER: ["serial_number", "Serial Number"],
    XiaomiVacuumProperty.VOICE_PACKET_ID: ["voice_packet_id", "Voice Packet Id"],
    XiaomiVacuumProperty.TIMEZONE: ["timezone", "Timezone"],
    XiaomiVacuumProperty.MAIN_BRUSH_TIME_LEFT: [
        "main_brush_time_left",
        "Main Brush  Time Left",
    ],
    XiaomiVacuumProperty.MAIN_BRUSH_LEFT: ["main_brush_left", "Main Brush Left"],
    XiaomiVacuumProperty.SIDE_BRUSH_TIME_LEFT: [
        "side_brush_time_left",
        "Side Brush Time Left",
    ],
    XiaomiVacuumProperty.SIDE_BRUSH_LEFT: ["side_brush_left", "Side Brush Left"],
    XiaomiVacuumProperty.FILTER_LEFT: ["filter_left", "Filter Left"],
    XiaomiVacuumProperty.FILTER_TIME_LEFT: ["filter_time_left", "Filter Time Left"],
    XiaomiVacuumProperty.FIRST_CLEANING_DATE: [
        "first_cleaning_date",
        "First Cleaning Date",
    ],
    XiaomiVacuumProperty.TOTAL_CLEANING_TIME: [
        "total_cleaning_time",
        "Total Cleaning Time",
    ],
    XiaomiVacuumProperty.CLEANING_COUNT: ["cleaning_count", "Cleaning Count"],
    XiaomiVacuumProperty.TOTAL_CLEANED_AREA: [
        "total_cleaned_area",
        "Total Cleaned Area",
    ],
    XiaomiVacuumProperty.SENSOR_DIRTY_LEFT: ["sensor_dirty_left", "Sensor Dirty Left"],
    XiaomiVacuumProperty.SENSOR_DIRTY_TIME_LEFT: [
        "sensor_dirty_time_left",
        "Sensor Dirty Time Left",
    ],
    XiaomiVacuumProperty.SECONDARY_FILTER_LEFT: ["secondary_filter_left", "Secondary Filter Left"],
    XiaomiVacuumProperty.SECONDARY_FILTER_TIME_LEFT: ["secondary_filter_time_left", "Secondary Filter Time Left"],
    XiaomiVacuumProperty.MOP_PAD_LEFT: ["mop_pad_left", "Mop Pad Left"],
    XiaomiVacuumProperty.MOP_PAD_TIME_LEFT: ["mop_pad_time_left", "Mop Pad Time Left"],
    XiaomiVacuumProperty.SILVER_ION_LEFT: ["silver_ion_left", "Silver-ion Left"],
    XiaomiVacuumProperty.SILVER_ION_TIME_LEFT: ["silver_ion_time_left", "Silver-ion Time Left"],
    XiaomiVacuumProperty.DETERGENT_LEFT: ["detergent_left", "Detergent Left"],
    XiaomiVacuumProperty.DETERGENT_TIME_LEFT: ["detergent_time_left", "Detergent Time Left"],
}

ACTION_TO_NAME: Final = {
    XiaomiVacuumAction.START: ["start", "Start"],
    XiaomiVacuumAction.PAUSE: ["pause", "Pause"],
    XiaomiVacuumAction.CHARGE: ["charge", "Charge"],
    XiaomiVacuumAction.START_CUSTOM: ["start_custom", "Start Custom"],
    XiaomiVacuumAction.STOP: ["stop", "Stop"],
    XiaomiVacuumAction.CLEAR_WARNING: ["clear_warning", "Clear Warning"],
    XiaomiVacuumAction.REQUEST_MAP: ["request_map", "Request Map"],
    XiaomiVacuumAction.UPDATE_MAP_DATA: ["update_map_data", "Update Map Data"],
    XiaomiVacuumAction.LOCATE: ["locate", "Locate"],
    XiaomiVacuumAction.TEST_SOUND: ["test_sound", "Test Sound"],
    XiaomiVacuumAction.RESET_MAIN_BRUSH: ["reset_main_brush", "Reset Main Brush"],
    XiaomiVacuumAction.RESET_SIDE_BRUSH: ["reset_side_brush", "Reset Side Brush"],
    XiaomiVacuumAction.RESET_FILTER: ["reset_filter", "Reset Filter"],
    XiaomiVacuumAction.RESET_SENSOR: ["reset_sensor", "Reset Sensor"],
    XiaomiVacuumAction.START_AUTO_EMPTY: ["start_auto_empty", "Start Auto Empty"],
    XiaomiVacuumAction.RESET_MOP_PAD: ["reset_mop_pad", "Reset Mop Pad"],
    XiaomiVacuumAction.RESET_SILVER_ION: ["reset_silver_ion", "Reset Silver-ion"],
    XiaomiVacuumAction.RESET_DETERGENT: ["reset_detergent", "Reset Detergent"],
}

STATE_CODE_TO_STATE: Final = {
    XiaomiVacuumState.UNKNOWN: STATE_UNKNOWN,
    XiaomiVacuumState.SWEEPING: STATE_SWEEPING,
    XiaomiVacuumState.IDLE: STATE_IDLE,
    XiaomiVacuumState.PAUSED: STATE_PAUSED,
    XiaomiVacuumState.ERROR: STATE_ERROR,
    XiaomiVacuumState.RETURNING: STATE_RETURNING,
    XiaomiVacuumState.CHARGING: STATE_CHARGING,
    XiaomiVacuumState.MOPPING: STATE_MOPPING,
    XiaomiVacuumState.DRYING: STATE_DRYING,
    XiaomiVacuumState.WASHING: STATE_WASHING,
    XiaomiVacuumState.RETURNING_WASHING: STATE_RETURNING_WASHING,
    XiaomiVacuumState.BUILDING: STATE_BUILDING,
    XiaomiVacuumState.SWEEPING_AND_MOPPING: STATE_SWEEPING_AND_MOPPING,
    XiaomiVacuumState.CHARGING_COMPLETED: STATE_CHARGING_COMPLETED,
    XiaomiVacuumState.UPGRADING: STATE_UPGRADING,
}

# Xiaomi Vacuum suction level names
SUCTION_LEVEL_CODE_TO_NAME: Final = {
    XiaomiVacuumSuctionLevel.QUIET: SUCTION_LEVEL_QUIET,
    XiaomiVacuumSuctionLevel.STANDARD: SUCTION_LEVEL_STANDARD,
    XiaomiVacuumSuctionLevel.STRONG: SUCTION_LEVEL_STRONG,
    XiaomiVacuumSuctionLevel.TURBO: SUCTION_LEVEL_TURBO,
}

# Xiaomi Vacuum water volume names
WATER_VOLUME_CODE_TO_NAME: Final = {
    XiaomiVacuumWaterVolume.LOW: WATER_VOLUME_LOW,
    XiaomiVacuumWaterVolume.MEDIUM: WATER_VOLUME_MEDIUM,
    XiaomiVacuumWaterVolume.HIGH: WATER_VOLUME_HIGH,
}

# Xiaomi Vacuum mop pad humidity names
MOP_PAD_HUMIDITY_CODE_TO_NAME: Final = {
    XiaomiVacuumMopPadHumidity.SLIGHTLY_DRY: MOP_PAD_HUMIDITY_SLIGHTLY_DRY,
    XiaomiVacuumMopPadHumidity.MOIST: MOP_PAD_HUMIDITY_MOIST,
    XiaomiVacuumMopPadHumidity.WET: MOP_PAD_HUMIDITY_WET,
}

# Xiaomi Vacuum cleaning mode names
CLEANING_MODE_CODE_TO_NAME: Final = {
    XiaomiVacuumCleaningMode.SWEEPING: CLEANING_MODE_SWEEPING,
    XiaomiVacuumCleaningMode.MOPPING: CLEANING_MODE_MOPPING,
    XiaomiVacuumCleaningMode.SWEEPING_AND_MOPPING: CLEANING_MODE_SWEEPING_AND_MOPPING,
}

WATER_TANK_CODE_TO_NAME: Final = {
    XiaomiVacuumWaterTank.INSTALLED: WATER_TANK_INSTALLED,
    XiaomiVacuumWaterTank.NOT_INSTALLED: WATER_TANK_NOT_INSTALLED,
    XiaomiVacuumWaterTank.MOP_INSTALLED: WATER_TANK_MOP_INSTALLED,
}

CARPET_SENSITIVITY_CODE_TO_NAME: Final = {
    XiaomiVacuumCarpetSensitivity.LOW: CARPET_SENSITIVITY_LOW,
    XiaomiVacuumCarpetSensitivity.MEDIUM: CARPET_SENSITIVITY_MEDIUM,
    XiaomiVacuumCarpetSensitivity.HIGH: CARPET_SENSITIVITY_HIGH,
}

TASK_STATUS_CODE_TO_NAME: Final = {
    XiaomiVacuumTaskStatus.COMPLETED: TASK_STATUS_COMPLETED,
    XiaomiVacuumTaskStatus.AUTO_CLEANING: TASK_STATUS_AUTO_CLEANING,
    XiaomiVacuumTaskStatus.ZONE_CLEANING: TASK_STATUS_ZONE_CLEANING,
    XiaomiVacuumTaskStatus.SEGMENT_CLEANING: TASK_STATUS_SEGMENT_CLEANING,
    XiaomiVacuumTaskStatus.SPOT_CLEANING: TASK_STATUS_SPOT_CLEANING,
    XiaomiVacuumTaskStatus.FAST_MAPPING: TASK_STATUS_FAST_MAPPING,
    XiaomiVacuumTaskStatus.AUTO_CLEANING_PAUSED: TASK_STATUS_AUTO_CLEANING_PAUSE,
    XiaomiVacuumTaskStatus.SEGMENT_CLEANING_PAUSED: TASK_STATUS_SEGMENT_CLEANING_PAUSE,
    XiaomiVacuumTaskStatus.ZONE_CLEANING_PAUSED: TASK_STATUS_ZONE_CLEANING_PAUSE,
    XiaomiVacuumTaskStatus.SPOT_CLEANING_PAUSED: TASK_STATUS_SPOT_CLEANING_PAUSE,
    XiaomiVacuumTaskStatus.MAP_CLEANING_PAUSED: TASK_STATUS_MAP_CLEANING_PAUSE,
    XiaomiVacuumTaskStatus.DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    XiaomiVacuumTaskStatus.MOPPING_PAUSED: TASK_STATUS_MOPPING_PAUSE,
    XiaomiVacuumTaskStatus.ZONE_MOPPING_PAUSED: TASK_STATUS_ZONE_MOPPING_PAUSE,
    XiaomiVacuumTaskStatus.SEGMENT_MOPPING_PAUSED: TASK_STATUS_SEGMENT_MOPPING_PAUSE,
    XiaomiVacuumTaskStatus.AUTO_MOPPING_PAUSED: TASK_STATUS_AUTO_MOPPING_PAUSE,
    XiaomiVacuumTaskStatus.AUTO_DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    XiaomiVacuumTaskStatus.ZONE_DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    XiaomiVacuumTaskStatus.SEGMENT_DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    XiaomiVacuumTaskStatus.MONITOR_CRUISE: TASK_STATUS_MONITOR_CRUISE,
    XiaomiVacuumTaskStatus.MONITOR_CRUISE_PAUSE: TASK_STATUS_MONITOR_CRUISE_PAUSE,
    XiaomiVacuumTaskStatus.MONITOR_SPOT: TASK_STATUS_MONITOR_SPOT,
    XiaomiVacuumTaskStatus.MONITOR_SPOT_PAUSE: TASK_STATUS_MONITOR_SPOT_PAUSE,
    XiaomiVacuumTaskStatus.SUMMON_CLEAN_PAUSE: TASK_STATUS_SUMMON_CLEAN_PAUSE,
    XiaomiVacuumTaskStatus.RETURNING_INSTALL_MOP: TASK_STATUS_RETURNING_INSTALL_MOP,
    XiaomiVacuumTaskStatus.RETURNING_REMOVE_MOP: TASK_STATUS_RETURNING_REMOVE_MOP,
}

STATUS_CODE_TO_NAME: Final = {
    XiaomiVacuumStatus.IDLE: STATE_IDLE,
    XiaomiVacuumStatus.PAUSED: STATE_PAUSED,
    XiaomiVacuumStatus.CLEANING: STATUS_CLEANING,
    XiaomiVacuumStatus.BACK_HOME: STATE_RETURNING,
    XiaomiVacuumStatus.PART_CLEANING: STATUS_SPOT_CLEANING,
    XiaomiVacuumStatus.FOLLOW_WALL: STATUS_FOLLOW_WALL,
    XiaomiVacuumStatus.CHARGING: STATUS_CHARGING,
    XiaomiVacuumStatus.OTA: STATUS_OTA,
    XiaomiVacuumStatus.FCT: STATUS_FCT,
    XiaomiVacuumStatus.WIFI_SET: STATUS_WIFI_SET,
    XiaomiVacuumStatus.POWER_OFF: STATUS_POWER_OFF,
    XiaomiVacuumStatus.FACTORY: STATUS_FACTORY,
    XiaomiVacuumStatus.ERROR: STATUS_ERROR,
    XiaomiVacuumStatus.REMOTE_CONTROL: STATUS_REMOTE_CONTROL,
    XiaomiVacuumStatus.SLEEPING: STATUS_SLEEP,
    XiaomiVacuumStatus.SELF_TEST: STATUS_SELF_TEST,
    XiaomiVacuumStatus.FACTORY_FUNCION_TEST: STATUS_FACTORY_FUNC_TEST,
    XiaomiVacuumStatus.STANDBY: STATUS_STANDBY,
    XiaomiVacuumStatus.SEGMENT_CLEANING: STATUS_SEGMENT_CLEANING,
    XiaomiVacuumStatus.ZONE_CLEANING: STATUS_ZONE_CLEANING,
    XiaomiVacuumStatus.SPOT_CLEANING: STATUS_SPOT_CLEANING,
    XiaomiVacuumStatus.FAST_MAPPING: STATUS_FAST_MAPPING,
    XiaomiVacuumStatus.MONITOR_CRUISE: STATUS_MONITOR_CRUISE,
    XiaomiVacuumStatus.MONITOR_SPOT: STATUS_MONITOR_SPOT,
    XiaomiVacuumStatus.SUMMON_CLEAN: STATUS_SUMMON_CLEAN,
}

RELOCATION_STATUS_CODE_TO_NAME: Final = {
    XiaomiVacuumRelocationStatus.LOCATED: RELOCATION_STATUS_LOCATED,
    XiaomiVacuumRelocationStatus.LOCATING: RELOCATION_STATUS_LOCATING,
    XiaomiVacuumRelocationStatus.FAILED: RELOCATION_STATUS_FAILED,
    XiaomiVacuumRelocationStatus.SUCCESS: RELOCATION_STATUS_SUCESS,
}

CHARGING_STATUS_CODE_TO_NAME: Final = {
    XiaomiVacuumChargingStatus.CHARGING: CHARGING_STATUS_CHARGING,
    XiaomiVacuumChargingStatus.NOT_CHARGING: CHARGING_STATUS_NOT_CHARGING,
    XiaomiVacuumChargingStatus.CHARGING_COMPLETED: CHARGING_STATUS_CHARGING_COMPLETED,
    XiaomiVacuumChargingStatus.RETURN_TO_CHARGE: CHARGING_STATUS_RETURN_TO_CHARGE,
}

ERROR_CODE_TO_ERROR_NAME: Final = {
    XiaomiVacuumErrorCode.NO_ERROR: ERROR_NO_ERROR,
    XiaomiVacuumErrorCode.DROP: ERROR_DROP,
    XiaomiVacuumErrorCode.CLIFF: ERROR_CLIFF,
    XiaomiVacuumErrorCode.BUMPER: ERROR_BUMPER,
    XiaomiVacuumErrorCode.GESTURE: ERROR_GESTURE,
    XiaomiVacuumErrorCode.BUMPER_REPEAT: ERROR_BUMPER_REPEAT,
    XiaomiVacuumErrorCode.DROP_REPEAT: ERROR_DROP_REPEAT,
    XiaomiVacuumErrorCode.OPTICAL_FLOW: ERROR_OPTICAL_FLOW,
    XiaomiVacuumErrorCode.BOX: ERROR_NO_BOX,
    XiaomiVacuumErrorCode.TANKBOX: ERROR_NO_TANKBOX,
    XiaomiVacuumErrorCode.WATERBOX_EMPTY: ERROR_WATERBOX_EMPTY,
    XiaomiVacuumErrorCode.BOX_FULL: ERROR_BOX_FULL,
    XiaomiVacuumErrorCode.BRUSH: ERROR_BRUSH,
    XiaomiVacuumErrorCode.SIDE_BRUSH: ERROR_SIDE_BRUSH,
    XiaomiVacuumErrorCode.FAN: ERROR_FAN,
    XiaomiVacuumErrorCode.LEFT_WHEEL_MOTOR: ERROR_LEFT_WHEEL_MOTOR,
    XiaomiVacuumErrorCode.RIGHT_WHEEL_MOTOR: ERROR_RIGHT_WHEEL_MOTOR,
    XiaomiVacuumErrorCode.TURN_SUFFOCATE: ERROR_TURN_SUFFOCATE,
    XiaomiVacuumErrorCode.FORWARD_SUFFOCATE: ERROR_FORWARD_SUFFOCATE,
    XiaomiVacuumErrorCode.CHARGER_GET: ERROR_CHARGER_GET,
    XiaomiVacuumErrorCode.BATTERY_LOW: ERROR_BATTERY_LOW,
    XiaomiVacuumErrorCode.CHARGE_FAULT: ERROR_CHARGE_FAULT,
    XiaomiVacuumErrorCode.BATTERY_PERCENTAGE: ERROR_BATTERY_PERCENTAGE,
    XiaomiVacuumErrorCode.HEART: ERROR_HEART,
    XiaomiVacuumErrorCode.CAMERA_OCCLUSION: ERROR_CAMERA_OCCLUSION,
    XiaomiVacuumErrorCode.MOVE: ERROR_MOVE,
    XiaomiVacuumErrorCode.FLOW_SHIELDING: ERROR_FLOW_SHIELDING,
    XiaomiVacuumErrorCode.INFRARED_SHIELDING: ERROR_INFRARED_SHIELDING,
    XiaomiVacuumErrorCode.CHARGE_NO_ELECTRIC: ERROR_CHARGE_NO_ELECTRIC,
    XiaomiVacuumErrorCode.BATTERY_FAULT: ERROR_BATTERY_FAULT,
    XiaomiVacuumErrorCode.FAN_SPEED_ERROR: ERROR_FAN_SPEED_ERROR,
    XiaomiVacuumErrorCode.LEFTWHELL_SPEED: ERROR_LEFTWHELL_SPEED,
    XiaomiVacuumErrorCode.RIGHTWHELL_SPEED: ERROR_RIGHTWHELL_SPEED,
    XiaomiVacuumErrorCode.BMI055_ACCE: ERROR_BMI055_ACCE,
    XiaomiVacuumErrorCode.BMI055_GYRO: ERROR_BMI055_GYRO,
    XiaomiVacuumErrorCode.XV7001: ERROR_XV7001,
    XiaomiVacuumErrorCode.LEFT_MAGNET: ERROR_LEFT_MAGNET,
    XiaomiVacuumErrorCode.RIGHT_MAGNET: ERROR_RIGHT_MAGNET,
    XiaomiVacuumErrorCode.FLOW_ERROR: ERROR_FLOW_ERROR,
    XiaomiVacuumErrorCode.INFRARED_FAULT: ERROR_INFRARED_FAULT,
    XiaomiVacuumErrorCode.CAMERA_FAULT: ERROR_CAMERA_FAULT,
    XiaomiVacuumErrorCode.STRONG_MAGNET: ERROR_STRONG_MAGNET,
    XiaomiVacuumErrorCode.WATER_PUMP: ERROR_WATER_PUMP,
    XiaomiVacuumErrorCode.RTC: ERROR_RTC,
    XiaomiVacuumErrorCode.AUTO_KEY_TRIG: ERROR_AUTO_KEY_TRIG,
    XiaomiVacuumErrorCode.P3V3: ERROR_P3V3,
    XiaomiVacuumErrorCode.CAMERA_IDLE: ERROR_CAMERA_IDLE,
    XiaomiVacuumErrorCode.BLOCKED: ERROR_BLOCKED,
    XiaomiVacuumErrorCode.LDS_ERROR: ERROR_LDS_ERROR,
    XiaomiVacuumErrorCode.LDS_BUMPER: ERROR_LDS_BUMPER,
    XiaomiVacuumErrorCode.WATER_PUMP_2: ERROR_WATER_PUMP,
    XiaomiVacuumErrorCode.FILTER_BLOCKED: ERROR_FILTER_BLOCKED,
    XiaomiVacuumErrorCode.EDGE: ERROR_EDGE,
    XiaomiVacuumErrorCode.CARPET: ERROR_CARPET,
    XiaomiVacuumErrorCode.LASER: ERROR_LASER,
    XiaomiVacuumErrorCode.EDGE_2: ERROR_EDGE,
    XiaomiVacuumErrorCode.ULTRASONIC: ERROR_ULTRASONIC,
    XiaomiVacuumErrorCode.NO_GO_ZONE: ERROR_NO_GO_ZONE,
    XiaomiVacuumErrorCode.ROUTE: ERROR_ROUTE,
    XiaomiVacuumErrorCode.ROUTE_2: ERROR_ROUTE,
    XiaomiVacuumErrorCode.BLOCKED_2: ERROR_BLOCKED,
    XiaomiVacuumErrorCode.BLOCKED_3: ERROR_BLOCKED,
    XiaomiVacuumErrorCode.RESTRICTED: ERROR_RESTRICTED,
    XiaomiVacuumErrorCode.RESTRICTED_2: ERROR_RESTRICTED,
    XiaomiVacuumErrorCode.RESTRICTED_3: ERROR_RESTRICTED,
    XiaomiVacuumErrorCode.REMOVE_MOP: ERROR_REMOVE_MOP,
    XiaomiVacuumErrorCode.MOP_REMOVED: ERROR_MOP_REMOVED,
    XiaomiVacuumErrorCode.MOP_REMOVED_2: ERROR_MOP_REMOVED,
    XiaomiVacuumErrorCode.MOP_PAD_STOP_ROTATE: ERROR_MOP_PAD_STOP_ROTATE,
    XiaomiVacuumErrorCode.MOP_PAD_STOP_ROTATE_2: ERROR_MOP_PAD_STOP_ROTATE,
    XiaomiVacuumErrorCode.BIN_FULL: ERROR_BIN_FULL,
    XiaomiVacuumErrorCode.BIN_OPEN: ERROR_BIN_OPEN,
    XiaomiVacuumErrorCode.BIN_OPEN_2: ERROR_BIN_OPEN,
    XiaomiVacuumErrorCode.WATER_TANK: ERROR_WATER_TANK,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK: ERROR_DIRTY_WATER_TANK,
    XiaomiVacuumErrorCode.WATER_TANK_DRY: ERROR_WATER_TANK_DRY,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_2: ERROR_DIRTY_WATER_TANK,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_BLOCKED: ERROR_DIRTY_WATER_TANK_BLOCKED,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_PUMP: ERROR_DIRTY_WATER_TANK_PUMP,
    XiaomiVacuumErrorCode.MOP_PAD: ERROR_MOP_PAD,
    XiaomiVacuumErrorCode.WET_MOP_PAD: ERROR_WET_MOP_PAD,
    XiaomiVacuumErrorCode.CLEAN_MOP_PAD: ERROR_CLEAN_MOP_PAD,
    XiaomiVacuumErrorCode.CLEAN_TANK_LEVEL: ERROR_CLEAN_TANK_LEVEL,
    XiaomiVacuumErrorCode.DIRTY_TANK_LEVEL: ERROR_DIRTY_TANK_LEVEL,
    XiaomiVacuumErrorCode.WASHBOARD_LEVEL: ERROR_WASHBOARD_LEVEL,
}

DUST_COLLECTION_TO_NAME: Final = {
    XiaomiVacuumDustCollection.NOT_AVAILABLE: DUST_COLLECTION_NOT_AVAILABLE,
    XiaomiVacuumDustCollection.AVAILABLE: DUST_COLLECTION_AVAILABLE,
}

AUTO_EMPTY_STATUS_TO_NAME: Final = {
    XiaomiVacuumAutoEmptyStatus.IDLE: STATE_IDLE,
    XiaomiVacuumAutoEmptyStatus.ACTIVE: AUTO_EMPTY_STATUS_ACTIVE,
    XiaomiVacuumAutoEmptyStatus.NOT_PERFORMED: AUTO_EMPTY_STATUS_NOT_PERFORMED,
}

SELF_WASH_BASE_STATUS_TO_NAME: Final = {
    XiaomiVacuumSelfWashBaseStatus.IDLE: STATE_IDLE,
    XiaomiVacuumSelfWashBaseStatus.WASHING: SELF_WASH_BASE_STATUS_WASHING,
    XiaomiVacuumSelfWashBaseStatus.DRYING: SELF_WASH_BASE_STATUS_DRYING,
    XiaomiVacuumSelfWashBaseStatus.PAUSED: SELF_WASH_BASE_STATUS_PAUSED,
    XiaomiVacuumSelfWashBaseStatus.RETURNING: SELF_WASH_BASE_STATUS_RETURNING,
    XiaomiVacuumSelfWashBaseStatus.CLEAN_ADD_WATER: SELF_WASH_BASE_STATUS_CLEAN_ADD_WATER,
    XiaomiVacuumSelfWashBaseStatus.ADDING_WATER: SELF_WASH_BASE_STATUS_ADDING_WATER,
}

SELF_AREA_CLEAN_TO_NAME: Final = {
    XiaomiVacuumSelfCleanArea.FIVE_SQUARE_METERS: SELF_AREA_CLEAN_FIVE_SQUARE_METERS,
    XiaomiVacuumSelfCleanArea.TEN_SQUARE_METERS: SELF_AREA_CLEAN_TEN_SQUARE_METERS,
    XiaomiVacuumSelfCleanArea.FIFTEEN_SQUARE_METERS: SELF_AREA_CLEAN_FIFTEEN_SQUARE_METERS,
    XiaomiVacuumSelfCleanArea.SINGLE_ZONE: SELF_AREA_CLEAN_SINGLE_ZONE,
}

MOP_WASH_LEVEL_TO_NAME: Final = {
    XiaomiVacuumMopWashLevel.DEEP: MOP_WASH_LEVEL_DEEP,
    XiaomiVacuumMopWashLevel.DAILY: MOP_WASH_LEVEL_DAILY,
    XiaomiVacuumMopWashLevel.WATER_SAVING: MOP_WASH_LEVEL_WATER_SAVING,
}

MOPPING_TYPE_TO_NAME: Final = {
    XiaomiVacuumMoppingType.DEEP: MOPPING_TYPE_DEEP,
    XiaomiVacuumMoppingType.DAILY: MOPPING_TYPE_DAILY,
    XiaomiVacuumMoppingType.ACCURATE: MOPPING_TYPE_ACCURATE,
}

ERROR_CODE_TO_IMAGE_INDEX: Final = {
    XiaomiVacuumErrorCode.BUMPER: 1,
    XiaomiVacuumErrorCode.BUMPER_REPEAT: 1,
    XiaomiVacuumErrorCode.DROP: 2,
    XiaomiVacuumErrorCode.DROP_REPEAT: 2,
    XiaomiVacuumErrorCode.CLIFF: 3,
    XiaomiVacuumErrorCode.GESTURE: 15,
    XiaomiVacuumErrorCode.BRUSH: 4,
    XiaomiVacuumErrorCode.SIDE_BRUSH: 5,
    XiaomiVacuumErrorCode.LEFT_WHEEL_MOTOR: 6,
    XiaomiVacuumErrorCode.RIGHT_WHEEL_MOTOR: 6,
    XiaomiVacuumErrorCode.LEFTWHELL_SPEED: 6,
    XiaomiVacuumErrorCode.RIGHTWHELL_SPEED: 6,
    XiaomiVacuumErrorCode.TURN_SUFFOCATE: 7,
    XiaomiVacuumErrorCode.FORWARD_SUFFOCATE: 7,
    XiaomiVacuumErrorCode.BOX: 8,
    XiaomiVacuumErrorCode.BOX_FULL: 9,
    XiaomiVacuumErrorCode.FAN: 9,
    XiaomiVacuumErrorCode.FILTER_BLOCKED: 9,
    XiaomiVacuumErrorCode.CHARGE_FAULT: 12,
    XiaomiVacuumErrorCode.CHARGE_NO_ELECTRIC: 16,
    XiaomiVacuumErrorCode.BATTERY_FAULT: 29,
    XiaomiVacuumErrorCode.INFRARED_FAULT: 39,
    XiaomiVacuumErrorCode.LDS_ERROR: 48,
    XiaomiVacuumErrorCode.LDS_BUMPER: 49,
    XiaomiVacuumErrorCode.EDGE: 54,
    XiaomiVacuumErrorCode.EDGE_2: 54,
    XiaomiVacuumErrorCode.CARPET: 55,
    XiaomiVacuumErrorCode.ULTRASONIC: 58,
    XiaomiVacuumErrorCode.ROUTE: 61,
    XiaomiVacuumErrorCode.ROUTE_2: 62,
    XiaomiVacuumErrorCode.BLOCKED: 63,
    XiaomiVacuumErrorCode.BLOCKED_2: 63,
    XiaomiVacuumErrorCode.BLOCKED_3: 64,
    XiaomiVacuumErrorCode.RESTRICTED: 65,
    XiaomiVacuumErrorCode.RESTRICTED_2: 65,
    XiaomiVacuumErrorCode.RESTRICTED_3: 65,
    XiaomiVacuumErrorCode.MOP_REMOVED: 69,
    XiaomiVacuumErrorCode.MOP_PAD_STOP_ROTATE: 69,
    XiaomiVacuumErrorCode.MOP_PAD_STOP_ROTATE_2: 69,
    XiaomiVacuumErrorCode.BIN_FULL: 101,
    XiaomiVacuumErrorCode.BIN_FULL_2: 101,
    XiaomiVacuumErrorCode.BIN_OPEN: 102,
    XiaomiVacuumErrorCode.BIN_OPEN_2: 102,
    XiaomiVacuumErrorCode.WATER_TANK: 105,
    XiaomiVacuumErrorCode.CLEAN_TANK_LEVEL: 105,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK: 106,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_2: 106,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_BLOCKED: 106,
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_PUMP: 106,
    XiaomiVacuumErrorCode.DIRTY_TANK_LEVEL: 106,
    XiaomiVacuumErrorCode.WATER_TANK_DRY: 107,
    XiaomiVacuumErrorCode.MOP_PAD: 111,
    XiaomiVacuumErrorCode.WET_MOP_PAD: 111,
    XiaomiVacuumErrorCode.WASHBOARD_LEVEL: 111,
    XiaomiVacuumErrorCode.CLEAN_MOP_PAD: 114,
}

# Xiaomi Vacuum error descriptions
ERROR_CODE_TO_ERROR_DESCRIPTION: Final = {
    XiaomiVacuumErrorCode.NO_ERROR: ["No error", ""],
    XiaomiVacuumErrorCode.DROP: [
        "Wheels are suspended",
        "Please reposition the robot and restart.",
    ],
    XiaomiVacuumErrorCode.CLIFF: [
        "Cliff sensor error",
        "Please wipe the cliff sensor and start the cleanup away from the stairs.",
    ],
    XiaomiVacuumErrorCode.BUMPER: [
        "Collision sensor is stuck",
        "Please clean and gently tap the collision sensor.",
    ],
    XiaomiVacuumErrorCode.GESTURE: [
        "Robot is tilted",
        "Please move the robot to a level surface and start again.",
    ],
    XiaomiVacuumErrorCode.BUMPER_REPEAT: [
        "Collision sensor is stuck",
        "Please clean and gently tap the collision sensor.",
    ],
    XiaomiVacuumErrorCode.DROP_REPEAT: [
        "Wheels are suspended",
        "Please reposition the robot and restart.",
    ],
    XiaomiVacuumErrorCode.OPTICAL_FLOW: [
        "Optical flow sensor error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.BOX: [
        "Dust bin not installed",
        "Please install the dust bin and filter.",
    ],
    XiaomiVacuumErrorCode.TANKBOX: [
        "Water tank not installed",
        "Please install the water tank.",
    ],
    XiaomiVacuumErrorCode.WATERBOX_EMPTY: [
        "Water tank is empty",
        "Please will up the water tank",
    ],
    XiaomiVacuumErrorCode.BOX_FULL: [
        "The filter not dry or blocked",
        "Please check whether the filter has dried or needs to be cleaned.",
    ],
    XiaomiVacuumErrorCode.BRUSH: [
        "The main brush wrapped",
        "Please remove the main brush and clean its bristles and bearings.",
    ],
    XiaomiVacuumErrorCode.SIDE_BRUSH: [
        "The side brush wrapped",
        "Please remove and clean the side brush.",
    ],
    XiaomiVacuumErrorCode.FAN: [
        "The filter not dry or blocked",
        "Please check whether the filter has dried or needs to be cleaned.",
    ],
    XiaomiVacuumErrorCode.LEFT_WHEEL_MOTOR: [
        "The robot is stuck, or its left wheel may be blocked by foreign objects",
        "Check whether there is any object stuck in the main wheels and start the robot in a new position.",
    ],
    XiaomiVacuumErrorCode.RIGHT_WHEEL_MOTOR: [
        "The robot is stuck, or its right wheel may be blocked by foreign objects",
        "Check whether there is any object stuck in the main wheels and start the robot in a new position.",
    ],
    XiaomiVacuumErrorCode.TURN_SUFFOCATE: [
        "The robot is stuck, or cannot turn",
        "The robot may be blocked or stuck.",
    ],
    XiaomiVacuumErrorCode.FORWARD_SUFFOCATE: [
        "The robot is stuck, or cannot go forward",
        "The robot may be blocked or stuck.",
    ],
    XiaomiVacuumErrorCode.CHARGER_GET: [
        "Cannot find base",
        "Please check whether the power cord is plugged in correctly.",
    ],
    XiaomiVacuumErrorCode.BATTERY_LOW: [
        "Low battery",
        "Battery level is too low. Please charge.",
    ],
    XiaomiVacuumErrorCode.CHARGE_FAULT: [
        "Charging error",
        "Please use a dry cloth to wipe charging contacts of the robot and auto-empty base.",
    ],
    XiaomiVacuumErrorCode.BATTERY_PERCENTAGE: ["", ""],
    XiaomiVacuumErrorCode.HEART: [
        "Internal error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.CAMERA_OCCLUSION: [
        "Visual positioning sensor error",
        "Please clean the visual positioning sensor.",
    ],
    XiaomiVacuumErrorCode.MOVE: [
        "Move sensor error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.FLOW_SHIELDING: [
        "Optical sensor error",
        "Please wipe the optical sensor clean and restart.",
    ],
    XiaomiVacuumErrorCode.INFRARED_SHIELDING: [
        "Infrared shielding error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.CHARGE_NO_ELECTRIC: [
        "The charging dock is not powered on",
        "The charging dock is not powered on. Please check whether the power cord is plugged in correctly.",
    ],
    XiaomiVacuumErrorCode.BATTERY_FAULT: [
        "Battery temperature error",
        "Please wait until the battery temperature returns to normal.",
    ],
    XiaomiVacuumErrorCode.FAN_SPEED_ERROR: [
        "Fan speed sensor error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.LEFTWHELL_SPEED: [
        "Left wheel may be blocked by foreign objects",
        "Check whether there is any object stuck in the main wheels and start the robot in a new position.",
    ],
    XiaomiVacuumErrorCode.RIGHTWHELL_SPEED: [
        "Right wheel may be blocked by foreign objects",
        "Check whether there is any object stuck in the main wheels and start the robot in a new position.",
    ],
    XiaomiVacuumErrorCode.BMI055_ACCE: [
        "Accelerometer error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.BMI055_GYRO: [
        "Gyro error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.XV7001: [
        "Gyro error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.LEFT_MAGNET: [
        "Left magnet sensor error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.RIGHT_MAGNET: [
        "Right magnet sensor error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.FLOW_ERROR: [
        "Flow sensor error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.INFRARED_FAULT: [
        "Infrared error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.CAMERA_FAULT: [
        "Camera error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.STRONG_MAGNET: [
        "Strong magnetic field detected",
        "Strong magnetic field detected. Please start away from the virtual wall.",
    ],
    XiaomiVacuumErrorCode.WATER_PUMP: [
        "Water pump error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.RTC: ["RTC error", "Please try to restart the vacuum-mop."],
    XiaomiVacuumErrorCode.AUTO_KEY_TRIG: [
        "Internal error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.P3V3: [
        "Internal error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.CAMERA_IDLE: [
        "Internal error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.BLOCKED: [
        "Route notification",
        "Cleanup route is blocked, returning to the dock.",
    ],
    XiaomiVacuumErrorCode.LDS_ERROR: [
        "Laser distance sensor error",
        "Please check whether the laser distance sensor has any jammed items",
    ],
    XiaomiVacuumErrorCode.LDS_BUMPER: [
        "Laser distance sensor bumper error",
        "Please check whether the laser distance sensor bumper is jammed",
    ],
    XiaomiVacuumErrorCode.WATER_PUMP_2: [
        "Water pump error",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.FILTER_BLOCKED: [
        "The filter not dry or blocked",
        "Please check whether the filter has dried or needs to be cleaned",
    ],
    XiaomiVacuumErrorCode.EDGE: [
        "Edge sensor error",
        "Edge sensor error. Please check and clean it.",
    ],
    XiaomiVacuumErrorCode.CARPET: [
        "Please start the robot in non-carpet area.",
        "A carpet is detected under the robot when it is mopping. Please move the robot to another place and restart it.",
    ],
    XiaomiVacuumErrorCode.LASER: [
        "The 3D obstacle avoidance sensor is malfunctioning.",
        "Please try to clean the 3D obstacle avoidance sensor.",
    ],
    XiaomiVacuumErrorCode.EDGE_2: [
        "Edge sensor error",
        "Edge sensor error. Please check and clean it.",
    ],
    XiaomiVacuumErrorCode.ULTRASONIC: [
        "The ultrasonic sensor is malfunctioning.",
        "Please restart the robot and try it again.",
    ],
    XiaomiVacuumErrorCode.NO_GO_ZONE: [
        "No-Go zone or virtual wall detected.",
        "Please move the robot away from the area and restart.",
    ],
    XiaomiVacuumErrorCode.ROUTE: [
        "Unable to reach the specified area.",
        "Please ensure that all doors in the home are open and clear any obstacles along the path.",
    ],
    XiaomiVacuumErrorCode.ROUTE_2: [
        "Unable to reach the specified area.",
        "Please try to delete the restricted area in the path.",
    ],
    XiaomiVacuumErrorCode.BLOCKED_2: [
        "Cleanup route is blocked.",
        "Please ensure that all doors in the home are open and clear any obstacles around the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.BLOCKED_3: [
        "Cleanup route is blocked.",
        "Please try to delete the restricted area or move the vacuum-mop out of this area.",
    ],
    XiaomiVacuumErrorCode.RESTRICTED: [
        "Detected that the vacuum-mop is in a restricted area.",
        "Please move the vacuum-mop out of this area.",
    ],
    XiaomiVacuumErrorCode.RESTRICTED_2: [
        "Detected that the vacuum-mop is in a restricted area.",
        "Please move the vacuum-mop out of this area.",
    ],
    XiaomiVacuumErrorCode.RESTRICTED_3: [
        "Detected that the vacuum-mop is in a restricted area.",
        "Please move the vacuum-mop out of this area.",
    ],
    XiaomiVacuumErrorCode.REMOVE_MOP: [
        "Mopping completed. Please remove and clean the mop in time.",
        "",
    ],
    XiaomiVacuumErrorCode.MOP_REMOVED: [
        "The mop pad comes off during the cleaning task.",
        "The mop pads come off, install them before resuming working.",
    ],
    XiaomiVacuumErrorCode.MOP_REMOVED_2: [
        "The mop pad comes off during the cleaning task.",
        "The mop pads come off, install them before resuming working.",
    ],
    XiaomiVacuumErrorCode.MOP_PAD_STOP_ROTATE: [
        "Mop Pad Stops Rotating",
        "The mop pad has stopped rotating, please check.",
    ],
    XiaomiVacuumErrorCode.MOP_PAD_STOP_ROTATE_2: [
        "Mop Pad Stops Rotating",
        "The mop pad has stopped rotating, please check.",
    ],
    XiaomiVacuumErrorCode.BIN_FULL: [
        "The dust collection bag is full, or the air duct is blocked.",
        "The system detects that the dust collection bag is full, or the air duct is blocked.",
    ],
    XiaomiVacuumErrorCode.BIN_OPEN: [
        "The upper cover of auto-empty base is not closed, or the dust collection bag is not installed.",
        "The system detects that the upper cover of auto-empty base is not closed, or the dust collection bag is not installed.",
    ],
    XiaomiVacuumErrorCode.BIN_OPEN_2: [
        "The upper cover of auto-empty base is not closed, or the dust collection bag is not installed.",
        "The system detects that the upper cover of auto-empty base is not closed, or the dust collection bag is not installed.",
    ],
    XiaomiVacuumErrorCode.BIN_FULL_2: [
        "The dust collection bag is full, or the air duct is blocked.",
        "The system detects that the dust collection bag is full, or the air duct is blocked.",
    ],
    XiaomiVacuumErrorCode.WATER_TANK: [
        "The clean water tank is not installed.",
        "The clean water tank is not installed, please install it.",
    ],
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK: [
        "The dirty water tank is full or not installed.",
        "Check whether the dirty water tank is full and the dirty water tank is installed.",
    ],
    XiaomiVacuumErrorCode.WATER_TANK_DRY: [
        "Low water level in the clean water tank.",
        "Insufficient water in the fresh tank, please add water. Otherwise, the robot will not return to the base to have the mop pad cleaned during the cleaning task.",
    ],
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_BLOCKED: [
        "Dirty water tank blocked.",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.DIRTY_WATER_TANK_PUMP: [
        "Dirty water tank pump error.",
        "Please try to restart the vacuum-mop.",
    ],
    XiaomiVacuumErrorCode.MOP_PAD: [
        "The washboard is not installed properly.",
        "The washboard is not installed and the robot cannot return to the self-wash base. Please ensure that the washboard is installed and the clasps on both sides are tightly fastened.",
    ],
    XiaomiVacuumErrorCode.WET_MOP_PAD: [
        "The water level of the washboard is abnormal, please clean the washboard timely.",
        "The water level of the washboard is abnormal. Please clean it timely to avoid blockage. If the problem still cannot be solved, please contact customer service.",
    ],
    XiaomiVacuumErrorCode.CLEAN_MOP_PAD: [
        "The cleaning task is complete, please clean the mop pad washboard.",
        "Please clean the mop pad washboard in time to avoid stains or odor.",
    ],
    XiaomiVacuumErrorCode.CLEAN_TANK_LEVEL: [
        "Please fill the clean water tank.",
        "The water in the clean water tank is about to be used up. Check and fill the clean water tank promptly.",
    ],
    XiaomiVacuumErrorCode.DIRTY_TANK_LEVEL: [
        "The water level in the used water tank is too high.",
        "Please check if the used water tank is full.",
    ],
    XiaomiVacuumErrorCode.WASHBOARD_LEVEL: [
        "Water level in the washboard is too high.",
        "Please clean the used water tank and washboard in time.",
    ],
}

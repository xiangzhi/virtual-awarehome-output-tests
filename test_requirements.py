import os
from utils import read_sensor_logs


NUM_DOOR_SENSOR_OUTPUTS = 1
NUM_MOTION_SENSOR_OUTPUTS = 1
NUM_APPLIANCE_SENSOR_OUTPUTS = 1

# sanity checks
def test_log_files_exist():
    logs = read_sensor_logs("")
    assert len(logs) == NUM_APPLIANCE_SENSOR_OUTPUTS + NUM_MOTION_SENSOR_OUTPUTS + NUM_DOOR_SENSOR_OUTPUTS
    assert len(read_sensor_logs("door")) == NUM_DOOR_SENSOR_OUTPUTS
    assert len(read_sensor_logs("motion")) == NUM_MOTION_SENSOR_OUTPUTS
    assert len(read_sensor_logs("appliance")) == NUM_APPLIANCE_SENSOR_OUTPUTS
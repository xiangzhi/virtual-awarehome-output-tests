import pytest
from utils import read_sensor_logs

class TestAllSensors:

    sensor_logs = read_sensor_logs("motion")

    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_have_valid_params(self, log):
        for reading in log:
            param_types = [param["name"] for param in reading["params"]]
            assert "degC" in param_types or "motionStatus" in param_types or \
                "illuminance" in param_types or "alarmStatus" in param_types

    @pytest.mark.parametrize("log", sensor_logs)
    def test_at_least_one_reading(self, log):
        valid = False
        for reading in log:
            param_types = [param["name"] for param in reading["params"]]
            valid = valid or "motionStatus" in param_types
            if valid:
                break
        assert valid


    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_motion_valid(self, log):
        for reading in log:
            for param in reading["params"]:
                if param["name"] == "motionStatus":
                    assert param["value"] == '0' or param["value"] == '1'

    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_motion_event_based(self, log):
        past_value = None
        for reading in log:
            for param in reading["params"]:
                if param["name"] == "motionStatus":
                    assert past_value != param["value"]
                    past_value = param["value"]

    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_illuminance_valid(self, log):
        for reading in log:
            for param in reading["params"]:
                if param["name"] == "illuminance":
                    assert "." not in param["value"]
                    assert int(param["value"]) > 0

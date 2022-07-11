import pytest
from utils import read_sensor_logs

class TestAllSensors:

    sensor_logs = read_sensor_logs("door")

    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_have_valid_params(self, log):
        for reading in log:
            param_types = [param["name"] for param in reading["params"]]
            assert "degC" in param_types or "doorStatus" in param_types

    @pytest.mark.parametrize("log", sensor_logs)
    def test_at_least_one_reading(self, log):
        valid = False
        for reading in log:
            param_types = [param["name"] for param in reading["params"]]
            valid = valid or "doorStatus" in param_types
            if valid:
                break
        assert valid


    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_value_accurate(self, log):
        for reading in log:
            for param in reading["params"]:
                if param["name"] == "doorStatus":
                    assert param["value"] == '0' or param["value"] == '1'

    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_door_event_based(self, log):
        past_value = None
        for reading in log:
            for param in reading["params"]:
                if param["name"] == "doorStatus":
                    assert past_value != param["value"]
                    past_value = param["value"]
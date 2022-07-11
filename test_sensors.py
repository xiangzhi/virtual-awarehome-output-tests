import pytest
from utils import read_sensor_logs
import os
import datetime
import dateutil.parser

class TestAllSensors:

    sensor_logs = read_sensor_logs()

    @pytest.mark.parametrize("log", sensor_logs)
    def test_correct_format(self, log):
        assert type(log) is list
        for reading in log:
            assert type(reading) is dict
    
    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_have_valid_time(self, log):
        for reading in log:
            # make sure they exist
            assert "timeStamp" in reading
            assert "timeStampMs" in reading
            # make sure we can parse them
            assert reading["timeStampMs"] > 0
            assert type(reading["timeStampMs"]) is int
            dateutil.parser.isoparse(reading["timeStamp"])

    @pytest.mark.parametrize("log", sensor_logs)
    def test_readings_have_increasing_time(self, log):

        past_time_ms = -1
        past_time = None
        for n, reading in enumerate(log):
            curr_time_ms = reading["timeStampMs"]
            curr_time = dateutil.parser.isoparse(reading["timeStamp"])
            if past_time_ms != -1:
                assert curr_time_ms > past_time_ms
                assert curr_time > past_time
            past_time_ms = curr_time_ms
            past_time = curr_time



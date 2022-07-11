import json
import os

valid_types = ["door", "motion", "appliance", ""]

def read_sensor_logs(type:str = "") -> list:

    if type not in valid_types:
        raise Exception(f"invalid type {type}")

    sensor_logs = []
    for log_path in os.listdir("example_outputs"):
        # filter the paths
        if type != "":
            if log_path.split(".")[-2] != type:
                continue

        with open(os.path.join("example_outputs", log_path), 'r') as f:
            data = json.load(f)

            # special case to bridge the actual sensors with the
            # format we want in virtual home
            if "readings" in data:
                sensor_logs.append(data["readings"])
            else:
                sensor_logs.append(data)
    return sensor_logs

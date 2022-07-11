## How to run the tests
1. Place the test files in the `example_outputs` directory.
2. Make sure the test files ends with the type of sensors and json file extension (e.g., `motion.json`).
    - `filname.motion.json` for motion sensors.
    - `filname.door.json` for door sensors.
    - `filname.appliance.json` for appliance sensors.
3. Update the number of test files in `test_requirements.py`. This steps is optional but it helps verify that the files are loaded correctly.
4. run pytest with `.pytest`.

## Dependencies:
- python-dateutil
- pytest
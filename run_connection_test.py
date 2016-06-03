import os
import json
from comport.tester import Tester

current_path = os.path.abspath(os.path.dirname("__file__"))

# load config
config_path = os.path.join(current_path, 'config.json')

if not os.path.exists(config_path):
    print("ERROR: No config file found!")
else:
    with open(config_path) as config_file:
        config_values = json.load(config_file)

    # start the connection tester
    tester = Tester(config_values)
    tester.check_connection()

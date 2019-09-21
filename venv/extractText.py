import json


with open('run_results.json', 'w') as json_data:
    data = json.load(json_data)
    json.dump(data, json_data)
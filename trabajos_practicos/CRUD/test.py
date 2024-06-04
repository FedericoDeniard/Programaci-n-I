import json

with open('config.json','r') as config:
    content = json.load(config)
    last_id = content["last_id"]
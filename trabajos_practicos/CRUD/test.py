import json


def get_config(path: str) -> dict:
    with open(path,'r') as config:
        content = json.load(config)
    return content

def save_config(path: str, data: dict):
    with open(path,'w') as config:
        config = json.dump(data,config,indent=2)

print(get_config('config.json'))
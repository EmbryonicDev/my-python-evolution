import json


def fileReader(filename: str):
    with open(filename) as file:
        data = file.read()
    return json.loads(data)

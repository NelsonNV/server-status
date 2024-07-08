import json

def leer_json(file="server.json"):
    with open(file, "r") as lectura:
        data = json.load(lectura)
    return data


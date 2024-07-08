import json

def leer_json(file="server.json"):
    with open(file, "r") as lectura:
        data = json.load(lectura)
    return data


def agregar_dato(file="server.json", service_name="", dns="", ip="", alt=""):
    data = leer_json(file)

    nuevo_dato = {service_name: {"dns": dns, "ip": ip, "alt": alt}}

    data.update(nuevo_dato)

    with open(file, "w") as escritura:
        json.dump(data, escritura, indent=4)


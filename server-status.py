import json
from ping3 import ping, verbose_ping


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


def consulta_ping(host):
    request = ping(host)
    result = {"status": True, "time": request}
    if request is None or request is False:
        result = {"status": False, "time": "Sin conexion"}

    return result


def mostrar_mensaje(service_name, result):
    if result["status"]:
        print(f'[+] {service_name} time: {result["time"]}')
    elif not result["status"]:
        print(f'[-] {service_name} time: {result["time"]}')


if __name__ == "__main__":
    servidores = leer_json()
    for server in servidores:
        print(f"------[ {server} ]-------")
        for ip in servidores[server]:
            result = consulta_ping(servidores[server][ip])
            mostrar_mensaje(ip, result)

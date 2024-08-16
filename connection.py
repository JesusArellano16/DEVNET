from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

load_dotenv()
user=os.getenv("USERNAME")
pswd=os.getenv("PASSWORD")

with open("mgmt_ip_addresses.txt") as file:
    ipadd = file.read().strip()



# Se crea un diccionario para el dispositivo a conectar
cisco_device = {
       'device_type': 'cisco_xr', #device_type se obtiene en http://ktbyers.github.io/netmiko/PLATFORMS.html
       'host': ipadd,
       'username': user,
       'password': pswd,
       'port': 22,             # opcional, default 22
       'verbose': True         # opcional, default False
       }


def router_info():
       # conexión a dispositivo y regresa un objeto asignado a la conexión ssh
       connection = ConnectHandler(**cisco_device)

       # envio de comando y se obtiene la salida
       output = connection.send_command('sh version')
       print('\n',output)

       # cierre de conexón
       print('\nClosing connection......')
       connection.disconnect()
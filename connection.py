from netmiko import ConnectHandler

ipadd = input("Ingresa la IP del RMAC a respaldar: ")
user = input("Ingresa tu usuario: ")
pswd = input("Ingresa tu password: ")

# Se crea un diccionario para el dispositivo a conectar
cisco_device = {
       'device_type': 'cisco_xr', #device_type se obtiene en http://ktbyers.github.io/netmiko/PLATFORMS.html
       'host': ipadd,
       'username': user,
       'password': pswd,
       'port': 22,             # opcional, default 22
       'verbose': True         # opcional, default False
       }

# conexión a dispositivo y regresa un objeto asignado a la conexión ssh
connection = ConnectHandler(**cisco_device)

# envio de comando y se obtiene la salida
output = connection.send_command('sh version')
print('\n',output)

# cierre de conexón
print('\nClosing connection......')
connection.disconnect()
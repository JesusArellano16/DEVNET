import click
import connection
import os_detection
import variables
import ips_loc

device_type = ''
device = ''
@click.group()
def cli():
    "Respaldo Previo a Ventana de Mantenimiento"
    pass

@cli.group()
def backup():
    "Respaldo previo"

@backup.group()
def r9():
    "Respaldo Central R9"

@r9.command()
def urraza():
    "Respaldando Central Urraza R9"
    click.echo("\nRespaldando Central Urraza R9\n")
    os_detection.os_det()
    user, pswd = variables.amb_var()
    IPadd = ips_loc.get_ips("urraza", device)
    connection.router_info(user, pswd, IPadd, device_type)

@r9.command()
def sotelo():
    "Respaldando Central SOTELO R9"
    click.echo("\nRespaldando Central SOTELO R9\n")
    os_detection.os_det()
    user, pswd = variables.amb_var()
    IPadd = ips_loc.get_ips("sotelo", device)
    connection.router_info(user, pswd, IPadd, device_type)

@r9.command()
def maqueta():
    "Respaldando Maqueta Python"
    click.echo("\nRespaldando Maqueta Python\n")
    #os_detection.os_det()
    user, pswd = variables.amb_var()
    ciscoos, device_type, IPadd = ips_loc.get_ips("maqueta")
    connection.router_info(user, pswd, IPadd, device_type, ciscoos)

if __name__ == '__main__':
    cli()
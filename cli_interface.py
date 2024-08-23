import click
import connection
import os_detection

@click.group()
def cli():
    "Respaldo Previo a Ventana de Mantenimiento"
    pass

@cli.group()
def r9():
    "Respaldo Central R9"

@r9.command()
def urraza():
    "Respaldando Central Urraza R9"
    click.echo("\nRespaldando Central Urraza R9\n")
    os_detection.os_det()
    connection.router_info()

cli()
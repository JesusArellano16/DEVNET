import click
import connection

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
    connection.router_info()

cli()
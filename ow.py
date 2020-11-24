from get import *
from set import *
from clear import *
from swap import *
import click

__author__ = "Brandon Ly"


@click.group()
def cli():
    """
    A simple CLI for quickly changing and swapping text files.

    Intended for stream overlays using OBS
    """
    pass


cli.add_command(get)
cli.add_command(clear)
cli.add_command(swap)
cli.add_command(set)

cli()

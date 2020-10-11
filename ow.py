from get import *
from writer import *
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


cli.add_command(g)
cli.add_command(c)
cli.add_command(s)
cli.add_command(w)

cli()

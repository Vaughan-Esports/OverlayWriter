from files import *
from paths import *
import click


@click.group(invoke_without_command=True)
@click.pass_context
def get(ctx):
    """- get the contents of file(s)"""
    if ctx.invoked_subcommand is None:
        click.echo("Match Name: " + read(matchN))
        click.echo("Team 1 Name: " + read(team1F))
        click.echo("Team 1 Score: " + read(team1scoreF))
        click.echo("Team 2 Name: " + read(team2F))
        click.echo("Team 2 Score: " + read(team2scoreF))


@get.command()
def t1():
    """- print team 1's name"""
    click.echo("Team 1 Name: " + read(team1F))


@get.command()
def t1s():
    """- print team 1's score"""
    click.echo("Team 1 Score: " + read(team1scoreF))


@get.command()
def t2():
    """- print team 2's name"""
    click.echo("Team 2 Name: " + read(team2F))


@get.command()
def t2s():
    """- print team 2's score"""
    click.echo("Team 2 Score: " + read(team2scoreF))


@get.command()
def m():
    """- print the match name"""
    click.echo("Match Name: " + read(matchN))


@get.command()
def teams():
    """- print both team's names"""
    click.echo("Team 1 Name: " + read(team1F))
    click.echo("Team 2 Name: " + read(team2F))


@get.command()
def scores():
    """- print both team's scores"""
    click.echo("Team 1 Score: " + read(team1scoreF))
    click.echo("Team 2 Score: " + read(team2scoreF))

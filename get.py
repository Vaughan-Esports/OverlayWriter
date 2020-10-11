from files import *
from paths import *
import click


@click.group(invoke_without_command=True)
@click.pass_context
def g(ctx):
    """- get the contents of file(s)"""
    if ctx.invoked_subcommand is None:
        click.echo("Match Name: " + read(matchN))
        click.echo("Team 1 Name: " + read(team1F))
        click.echo("Team 1 Score: " + read(team1scoreF))
        click.echo("Team 2 Name: " + read(team2F))
        click.echo("Team 2 Score: " + read(team2scoreF))


@g.command()
def t1():
    """- print team 1's name"""
    click.echo("Team 1 Name: " + read(team1F))


@g.command()
def t1s():
    """- print team 1's score"""
    click.echo("Team 1 Score: " + read(team1scoreF))


@g.command()
def t2():
    """- print team 2's name"""
    click.echo("Team 2 Name: " + read(team2F))


@g.command()
def t2s():
    """- print team 2's score"""
    click.echo("Team 2 Score: " + read(team2scoreF))


@g.command()
def m():
    """- print the match name"""
    click.echo("Match Name: " + read(matchN))


@g.command()
def teams():
    """- print both team's names"""
    click.echo("Team 1 Name: " + read(team1F))
    click.echo("Team 2 Name: " + read(team2F))


@g.command()
def scores():
    """- print both team's scores"""
    click.echo("Team 1 Score: " + read(team1scoreF))
    click.echo("Team 2 Score: " + read(team2scoreF))

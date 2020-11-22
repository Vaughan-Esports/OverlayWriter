from files import *
from paths import *
import click


@click.group(invoke_without_command=True)
@click.pass_context
def clear(ctx):
    """- clear file(s)"""
    if ctx.invoked_subcommand is None:
        write(team1F, "")
        write(team2F, "")
        write(team1scoreF, "")
        write(team2scoreF, "")
        write(matchN, "")
        click.echo('Cleared all files')


@clear.command()
def t1():
    """- clear team 1's name"""
    write(team1F, "")
    click.echo('Cleared team 1\'s name')


@clear.command()
def t1s():
    """- clear team 1's score"""
    write(team1scoreF, "")
    click.echo('Cleared team 1\'s score')


@clear.command()
def t2():
    """- clear team 2's name"""
    write(team2F, "")
    click.echo('Cleared team 2\' name')


@clear.command()
def t2s():
    """- clear team 2's score"""
    write(team2scoreF, "")
    click.echo('Cleared team 2\'s score')


@clear.command()
def m():
    """- clear match name"""
    write(matchN, "")
    click.echo('Cleared the match name')

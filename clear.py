from files import *
from config import *
from rich import print as rprint
import click


@click.group(invoke_without_command=True)
@click.pass_context
def clear(ctx):
    """- clear file(s)"""
    if ctx.invoked_subcommand is None:
        ctx.invoke(t1)
        ctx.invoke(t1s)
        ctx.invoke(t2)
        ctx.invoke(t2s)
        ctx.invoke(match)


@clear.command()
def t1():
    """- clear team 1's name"""
    write(team1F, "")
    rprint(f"{main_colour}Cleared team {t1_colour}1\'s {main_colour}name.")


@clear.command()
def t1s():
    """- clear team 1's score"""
    write(team1scoreF, "")
    rprint(f"{main_colour}Cleared team {t1_colour}1\'s {main_colour}score.")


@clear.command()
def t2():
    """- clear team 2's name"""
    write(team2F, "")
    rprint(f"{main_colour}Cleared team {t2_colour}2\'s {main_colour}name.")


@clear.command()
def t2s():
    """- clear team 2's score"""
    write(team2scoreF, "")
    rprint(f"{main_colour}Cleared team {t2_colour}2\'s {main_colour}score.")


@clear.command()
def match():
    """- clear match name"""
    write(matchN, "")
    rprint(f"{main_colour}Cleared match name.")

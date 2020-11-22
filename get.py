from files import *
from config import *
from rich import print as rprint
import click


@click.group(invoke_without_command=True)
@click.pass_context
def get(ctx):
    """- get the contents of file(s)"""
    if ctx.invoked_subcommand is None:
        ctx.invoke(match)
        ctx.invoke(t1)
        ctx.invoke(t1s)
        ctx.invoke(t2)
        ctx.invoke(t2s)


@get.command()
def t1():
    """- print team 1's name"""
    rprint(f"{main_colour}Team {t1_colour}1 {main_colour}Name: {arg_colour}{read(team1F)}")


@get.command()
def t1s():
    """- print team 1's score"""
    rprint(f"{main_colour}Team {t1_colour}1 {main_colour}Score: {arg_colour}{read(team1scoreF)}")


@get.command()
def t2():
    """- print team 2's name"""
    rprint(f"{main_colour}Team {t2_colour}2 {main_colour}Name: {arg_colour}{read(team2F)}")


@get.command()
def t2s():
    """- print team 2's score"""
    rprint(f"{main_colour}Team {t2_colour}2 {main_colour}Score: {arg_colour}{read(team2scoreF)}")


@get.command()
def match():
    """- print the match name"""
    rprint(f"{main_colour}Match Name: [green]{read(matchN)}")


@get.command()
@click.pass_context
def teams(ctx):
    """- print both team's names"""
    ctx.invoke(t1)
    ctx.invoke(t2)


@get.command()
@click.pass_context
def scores(ctx):
    """- print both team's scores"""
    ctx.invoke(t1s)
    ctx.invoke(t2s)

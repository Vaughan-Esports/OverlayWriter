from files import *
from paths import *
from rich import print as rprint
import click


@click.group()
def writer():
    """- write to file(s)"""
    pass


@writer.command()
@click.argument('name', nargs=-1)
def t1(name):
    """- change team 1's name"""
    write(team1F, " ".join(name))
    rprint(f"[magenta]Team 1 Name: [green]{read(team1F)}")


@writer.command()
@click.argument('score')
def t1s(score):
    """- change team 1's score"""
    write(team1scoreF, score)
    rprint(f"[magenta]Team 1 Score: [green]{read(team1scoreF)}")


@writer.command()
@click.argument('name', nargs=-1)
def t2(name):
    """- change team 2's name"""
    write(team2F, " ".join(name))
    rprint(f"[magenta] Team 2 Name: [green]{read(team2F)}")


@writer.command()
@click.argument('score')
def t2s(score):
    """- change team 2's score"""
    write(team2scoreF, score)
    rprint(f"[magenta]Team 2 Score: [green]{read(team2scoreF)}")


@writer.command()
@click.argument('match')
def m(match):
    """- change the match name"""
    write(matchN, " ".join(match))
    rprint(f"[magenta]Match Name: [green]{read(matchN)}")

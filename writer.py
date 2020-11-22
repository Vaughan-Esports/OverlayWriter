from files import *
from config import *
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
    rprint(f"{main_colour}Team {t1_colour}1 Name: {arg_colour}{read(team1F)}")


@writer.command()
@click.argument('score')
def t1s(score):
    """- change team 1's score"""
    write(team1scoreF, score)
    rprint(f"{main_colour}Team {t1_colour}1 Score: {arg_colour}{read(team1scoreF)}")


@writer.command()
@click.argument('name', nargs=-1)
def t2(name):
    """- change team 2's name"""
    write(team2F, " ".join(name))
    rprint(f"{main_colour} Team {t2_colour}2 Name: {arg_colour}{read(team2F)}")


@writer.command()
@click.argument('score')
def t2s(score):
    """- change team 2's score"""
    write(team2scoreF, score)
    rprint(f"{main_colour}Team {t2_colour}2 Score: {arg_colour}{read(team2scoreF)}")


@writer.command()
@click.argument('match')
def m(match):
    """- change the match name"""
    write(matchN, " ".join(match))
    rprint(f"{main_colour}Match Name: {arg_colour}{read(matchN)}")

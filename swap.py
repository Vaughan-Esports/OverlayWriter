from files import *
from paths import *
import click


@click.group(invoke_without_command=True)
@click.pass_context
def swap(ctx):
    """- swap the text in file(s)"""
    if ctx.invoked_subcommand is None:
        team1_name = read(team1F)
        team2_name = read(team2F)
        team1_score = read(team1scoreF)
        team2_score = read(team2scoreF)
        write(team1F, team2_name)
        write(team1scoreF, team2_score)
        write(team2F, team1_name)
        write(team2scoreF, team1_score)


@swap.command()
def teams():
    """- swap team names"""
    team1_name = read(team1F)
    team2_name = read(team2F)
    write(team1F, team2_name)
    write(team2F, team1_name)


@swap.command()
def scores():
    """- swap team scores"""
    team1_score = read(team1scoreF)
    team2_score = read(team2scoreF)
    write(team1scoreF, team2_score)
    write(team2scoreF, team1_score)

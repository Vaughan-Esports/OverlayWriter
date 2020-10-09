import click

__author__ = "Brandon Ly"

# all text files
team1F = "textFiles/team1.txt"
team2F = "textFiles/team2.txt"
team1scoreF = "textFiles/team1score.txt"
team2scoreF = "textFiles/team2score.txt"
matchN = "textFiles/match.txt"


@click.group()
def main():
    """
    Simple CLI for quickly changing text files intended for stream overlays using OBS
    """
    pass


@click.command()
@click.argument('name')
def t1(name):
    """- Change team 1's name"""
    f = open(str(team1F), "w")
    f.write(str(name))
    f.close()


@click.command()
@click.argument('score')
def t1s(score):
    """- Change team 1's score"""
    f = open(str(team1scoreF), "w")
    f.write(str(score))
    f.close()


@click.command()
@click.argument('name')
def t2(name):
    """- Change team 2's name"""
    f = open(str(team2F), "w")
    f.write(str(name))
    f.close()


@click.command()
@click.argument('score')
def t2s(score):
    """- Change team 2's score"""
    f = open(str(team2scoreF), "w")
    f.write(str(score))
    f.close()


@click.command()
@click.argument('match')
def m(match):
    """- Change the match name"""
    f = open(str(matchN), "w")
    f.write(str(matchN))
    f.close()


main.add_command(t1)
main.add_command(t1s)
main.add_command(t2)
main.add_command(t2s)
main.add_command(m)

if __name__ == '__main__':
    main()

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
    write(str(team1F), name)


@click.command()
@click.argument('score')
def t1s(score):
    """- Change team 1's score"""
    write(str(team1scoreF), score)


@click.command()
@click.argument('name')
def t2(name):
    """- Change team 2's name"""
    write(str(team2F), name)


@click.command()
@click.argument('score')
def t2s(score):
    """- Change team 2's score"""
    write(str(team2scoreF), score)


@click.command()
@click.argument('match')
def m(match):
    """- Change the match name"""
    write(str(matchN), match)


@click.command()
def swap():
    """- Swaps the team name and scores"""
    team1N = read(team1F)
    team2N = read(team2F)
    team1S = read(team1scoreF)
    team2S = read(team2scoreF)


def write(file, string):
    f = open(str(file), "w")
    f.write(string)
    f.close()


def read(file):
    f = open(str(file), "r")
    string = f.read()
    f.close()
    return string


main.add_command(t1)
main.add_command(t1s)
main.add_command(t2)
main.add_command(t2s)
main.add_command(m)

if __name__ == '__main__':
    main()

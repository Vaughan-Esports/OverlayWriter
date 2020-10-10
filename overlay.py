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
    Simple CLI for quickly changing and swapping text files.

    Intended for stream overlays using OBS
    """
    pass


@click.command()
@click.argument('name')
def t1(name):
    """- Change team 1's name"""
    write(team1F, name)


@click.command()
@click.argument('score')
def t1s(score):
    """- Change team 1's score"""
    write(team1scoreF, score)


@click.command()
@click.argument('name')
def t2(name):
    """- Change team 2's name"""
    write(team2F, name)


@click.command()
@click.argument('score')
def t2s(score):
    """- Change team 2's score"""
    write(team2scoreF, score)


@click.command()
@click.argument('match')
def m(match):
    """- Change the match name"""
    write(matchN, match)


@click.command()
def swap():
    """- Swaps the team name and scores"""
    team1_name = read(team1F)
    team2_name = read(team2F)
    team1_score = read(team1scoreF)
    team2_score = read(team2scoreF)
    write(team1F, team2_name)
    write(team1scoreF, team2_score)
    write(team2F, team1_name)
    write(team2scoreF, team1_score)


@click.command()
def clear():
    """- Clears all files"""
    write(team1F, "")
    write(team2F, "")
    write(team1scoreF, "")
    write(team2scoreF, "")


def write(file, string):
    """
    Overwrites the content of a file with the given string
    :param file: file to be written to
    :param string: string to be written
    """
    f = open(str(file), "w")
    f.write(string)
    f.close()


def read(file):
    """
    Reads the current contents a file
    :param file: the file to be read
    :return: the contents of the file
    """
    f = open(str(file), "r")
    string = f.read()
    f.close()
    return string


main.add_command(t1)
main.add_command(t1s)
main.add_command(t2)
main.add_command(t2s)
main.add_command(m)
main.add_command(swap)
main.add_command(clear)

if __name__ == '__main__':
    main()

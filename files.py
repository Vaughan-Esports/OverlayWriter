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

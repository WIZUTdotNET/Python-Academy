
def loadFile(filename):

    content = ""
    file = open(filename, encoding="utf-8")

    with file as f:
        content += f.read()
        f.close()

    return(content)

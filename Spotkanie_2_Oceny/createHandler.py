
def loadFile(filename):
    content = ""
    with open(filename) as f:
        content += f.read() # każdy element to jeden wiersz
        f.close()
    return(content)

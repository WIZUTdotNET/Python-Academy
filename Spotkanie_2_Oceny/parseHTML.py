"""
** Modul przyjmuje plik html zapisanej strony z ocenami z e-dziekanatu
# NOTE: plik html musi byc przetworzony na ciag znaków (String)

** W module znajduja sie dwie funkcje,
* Pierwsza zwraca dwuwymiarowa liste w nastepujacym formacie:
    - lista[wiersz][kolumna]
    - lista[0][:] - zawiera naglowek tabeli
        skladajacy sie na nazwe przedmiotu, prowadzacego, oceny i ECTS
    - lista[1:][0] - lista przedmiotow
    - kazdy kolejny element (tj. lista[:][1:]) zawiera wartosci pol
* Druga funkcja zwraca tuple z informacjami o studencie:
    - [0] - Imie
    - [1] - Nazwisko
    - [2] - Nr albumu
"""
from bs4 import BeautifulSoup
import re

def getTable(handler):

    tagStart = '<table'
    tagStop = '</table>'

    indexStart = handler.find(tagStart)
    newString = handler[indexStart:]

    indexStop = newString.find(tagStop)
    newString = newString[:indexStop+len(tagStop)]

    soup = BeautifulSoup(newString, 'html.parser')
    rows = soup.find_all('tr')

    table = []

    for i in range(0, len(rows)-1):
        table.append([ td.text for td in soup.table('tr')[i]('td') ])

    return(table)

def getInfo(handler):

    tagStart = '<span id="ctl00_ctl00_ContentPlaceHolder_wumasterWhoIsLoggedIn" class="who_is_logged_in">'
    tagStop = '</span>'

    indexStart = handler.find(tagStart)
    newString = handler[indexStart+len(tagStart):]

    indexStop = newString.find(tagStop)
    newString = newString[:indexStop]
    ## NOTE: newList -> 'Imię Nazwisko - nr albumu: XXXXX'

    space,name,surname,id_number = 0,'','',''

    for i in range(0, len(newString)):
        if(re.search(r'\w', newString[i])!=None):
            if(space==0):
                name += newString[i]
            if(space==1):
                surname += newString[i]
        if(re.search(r' ', newString[i])!=None):
            space +=1
        if(re.search(r'\xe2', newString)!=None):
            space = 3
        if(re.search(r'\d', newString[i])!=None):
            id_number += newString[i]

    id_number = int(id_number)

    return (name,surname,id_number)

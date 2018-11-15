"""
Pierwsza funkcja zwraca set zawierajaca nazwy przedmiotow
Druga funkcja zwraca wartosc sredniej wazonej ocen
"""
from parseHTML import getTable
import re

def getItems(handler):

    table = getTable(handler)
    items = []

    for i in range(1, len(table)):
        items.append(table[i][0])

    return(set(items))

def getAVG(handler):

    table = getTable(handler)

    grades = []
    column = 5

    for i in range(1,len(table)-1):
        regex = re.sub('\d\d.\d\d.\d\d$', '', table[i][column])
        while(regex == '2'):
            column += 1
            regex = re.sub('\d\d.\d\d.\d\d$', '', table[i][column])
        grades.append(regex)
        column = 5

    sum = 0
    ects_sum = 0

    for i in range(0, len(table)-2):
        grades[i] = grades[i].replace(',','.')
        try:
            grades[i] = float(grades[i])
            sum += float(table[i+1][10])*grades[i]
            ects_sum += float(table[i+1][10])
        except:
            grades[i] == '0'

    value = sum/ects_sum

    return(round(value,2))

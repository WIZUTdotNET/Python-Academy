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
    
    for i in range(1, len(table)):
        if isinstance(table[i][column], float):
            while(table[i][column]==2.0):
                column+=1
            if isinstance(table[i][column], float):
                grades.append(table[i][column])
            else:
                grades.append(0)
            column = 5
        else:
            grades.append(0)

    sum = 0
    ects_sum = 0

    for i in range(len(table)-1):
        sum += float(table[i+1][10])*grades[i]
        ects_sum += float(table[i+1][10])

    value = sum/ects_sum

    return(round(value,2))

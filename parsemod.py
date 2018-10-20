"""
* Funkcja pobiera plik tekstowy z ocenami semestralnymi w edziekanacie
* Zwraca liste w nastepujacym formacie: 
    - pierwszy element - Imie studenta i nr albumu
    - drugi element    - Nazwy kolumn dla tabeli - 
    - kazdy kolejny element zawiera jeden wiersz w tabeli
      skladajacy sie na nazwe przedmiotu, prowadzacego, oceny i ECTS
"""
def parse_edziekanat_grades(filename):

    #Wczytaj zawartosc pliku do listy
    with open(filename) as f:
        #kazdy element zawiera jednen wiersz z pliku
        content = f.readlines()
        f.close()
    
    newList = []
    
    #Zmodyfikuj odczytana zawartosc aby usunac wiersze z datami
    #I zapisac kazdy wiersz pliku w jednej linijce (jednym elemencie tablicy)
    for i in range(0,len(content)-1): 
        import re
        m = re.search(r'\bocena\b\s\bkoncowa\b',content[i])
        if m != None:
            newList.append(content[i][:-1] + content[i+1][10:-1])
    
    retlist = []
    
    
    for i in newList:
        #pozbadz sie tabulacji z kazdego wiersza
        no_commas = i.split('\t')
        #Nowy wiersz zawiera niepotrzebne elementy - "puste miejsca"
        rows_list = [i for i in no_commas if i != " "]  
        
        #Do nowej listy dodaj zmodyfikowany wiersz, z ktorego wybieramy tylko 
        #Niektore kolumny - nazwy przedmiotu, prowadzacego, ostatnia otrzymana ocene i ECTS
        retlist.append([rows_list[0],rows_list[3],rows_list[-2],rows_list[-1]])
    
    #Przygotowanie wiersza z nazwami kolumn
    column_names = content[2].split('\t')
    
    #Zwracana lista
    return [[content[0]],[column_names[0],column_names[3],column_names[5],column_names[-1]]] + retlist
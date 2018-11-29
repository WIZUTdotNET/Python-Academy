import createHandler as chand
import parsemod as pd
import parseHTML as phtml
import getStudentInformation as gsi
import createPDF as cpdf
import createExcel as cxls
import os

#filename = "edziekanat_example.txt"
filename = "e-Dziekanat.html"
handler = chand.loadFile(filename)
info = phtml.getInfo(handler)
item_list = gsi.getItems(handler)
gradesAverage = gsi.getAVG(handler)

def hello():

    print('Hello in our program!!!')
    print('Hi ' + str(info[0]))
    print('Your student id: ' + str(info[2]))
    print('Your subjects this semester are: ')
    for i in range(0, len(list(item_list))):
        print(str(i+1) + '. ' + list(item_list)[i])
    print('Your weighted average of grades: ' + str(gradesAverage))

def create():

    #grades_list = pd.parse_edziekanat_grades(filename) ## NOTE: TXT parser
    grades_list = phtml.getTable(handler) ## NOTE: HTML parser
    pdf_file = cpdf.createPDFFile(info, item_list, gradesAverage)
    excel_file = cxls.createExcelFile(grades_list)

def check():

    if os.path.exists('raport.pdf'):
        print("We created PDF file")
    if os.path.exists('raport.xls'):
        print("We created Excel file")

if __name__ == "__main__":
    hello()
    create()
    check()

import parsemod as pd
import createPDF as cpdf
import createExcel as cxlsx

import os

filename = "edziekanat_example.txt"
#filename = "e-Dziekanat.html"

def hello():
    print('Hello in our program!!!')

def create():
    grades_list = pd.parse_edziekanat_grades(filename)
    pdf_file = cpdf.create_PDF_file(grades_list)
    excel_file = cxlsx.create_Excel_file(grades_list)

def check():
    if os.path.exists('raport.pdf'):
        print("We created PDF file")
    if os.path.exists('raport.xlsx'):
        print("We created Excel file")

if __name__ == "__main__":
    hello()
    create()
    check()

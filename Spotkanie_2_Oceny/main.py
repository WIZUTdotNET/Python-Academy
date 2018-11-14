import parsemod as pd
import createPDF as cpdf
import createExcel as cxlsx

filename = "edziekanat_przyklad.txt"

if __name__ == 'main':
    grades_list = pd.parse_edziekanat_grades(filename)
    pdf_file = cpdf.create_PDF_file(grades_list)
    excel_file = cxlsx.create_Excel_file(grades_list)
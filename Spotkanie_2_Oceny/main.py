import parsemod as pd
import createPDF as cpdf
import createExcel as cxlsx

filename = "edziekanat_example.txt"

if __name__ == "__main__":
    grades_list = pd.parse_edziekanat_grades(filename)
    pdf_file = cpdf.create_PDF_file(grades_list)
    excel_file = cxlsx.create_Excel_file(grades_list)
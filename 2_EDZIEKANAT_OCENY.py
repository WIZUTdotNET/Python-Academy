import parsemod as pd
from reportlab import *
from reportlab.lib.styles import *
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.lib import pagesizes
from reportlab.lib.pagesizes import portrait
from reportlab.pdfbase import pdfpattern
from reportlab.platypus.para import Paragraph



lista_ocen = pd.parse_edziekanat_grades("edziekanat_przyklad.txt")
print (lista_ocen)

"""
Przemek : tutaj moja proba tworzenia raportu w formacie pdf

https://stackoverflow.com/questions/10112244/convert-plain-text-to-pdf-in-python

# ------------------------------------
# Styles
# ------------------------------------



styleSheet = getSampleStyleSheet()
mystyle = ParagraphStyle(name='normal',fontName='Courier',
                         fontSize=10, 
                         alignment=TA_JUSTIFY, 
                         leading=1.2*12,
                         parent=styleSheet['Normal'])       

#=====================================================================================       
model_report = 'report.txt'


# Create document for writing to pdf   
doc = SimpleDocTemplate(str(pdfpattern),  
                        rightMargin=40, leftMargin=40, 
                        topMargin=40, bottomMargin=25,
                        pageSize=pagesizes.A4)
doc.pagesize = portrait(pagesizes.A4) 

# Container for 'Flowable' objects
elements = []    

# Open the model report
infile   = lista_ocen
report_paragraphs = lista_ocen

for para in report_paragraphs:  
    para1 = '<font face="Courier" >%s</font>' % para 
    elements.append(Paragraph(para1, style=styleSheet['Normal']))
doc.build(elements)

"""
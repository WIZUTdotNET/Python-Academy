import parsemod as pd
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica

"""
Interesting pdf - creation : 

http://www.devshed.com/c/a/Python/Python-for-PDF-Generation/
"""



lista_ocen = pd.parse_edziekanat_grades("edziekanat_przyklad.txt")

#Create new pdf document
pdf = Canvas("test.pdf", pagesize = letter)

#Set font and draw title
pdf.setFont("Courier-Bold", 14)
pdf.setStrokeColorRGB(1, 0, 0)
pdf.drawString(inch * 1, inch * 10, lista_ocen[0][0])


#set font for rows with grades
pdf.setFont("Courier-Bold", 12)
pdf.setStrokeColorRGB(1, 0, 0)
#create handle used to add lines to pdf 
table = pdf.beginText(inch * 1, inch * 9)


for x in lista_ocen[1:]:
    #join lines with tab and add them to table
    row = "    ".join(x)
    table.textLine(row)
    
weighted_sum = [a * b for a,b in zip([float(i[2].replace(',','.')) for i in lista_ocen[2:]],[float(i[3].replace(',','.')) for i in lista_ocen[2:]])]
table.textLine("Twoja srednia to:  {2.f}".format(str(sum(weighted_sum)/30)))

#draw all lines to pdf
pdf.drawText(table)
pdf.showPage()
pdf.save()
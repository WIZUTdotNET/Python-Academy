"""
Interesting pdf - creation :

http://www.devshed.com/c/a/Python/Python-for-PDF-Generation/

"""
# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet

def createPDFFile(info, item_list, gradesAverage):

    # Create new pdf document
    pdf = canvas.Canvas("raport.pdf", pagesize=A4)
    width, height = A4

    # Set font
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

    minus = 40
    pdf.setFont("Arial", 14)
    pdf.drawString(40,(height-minus), "Your name: " + str(info[0]) + " " + str(info[1]))
    minus += 40
    pdf.drawString(40,(height-minus), "Your student id: " + str(info[2]))
    minus += 40

    stylesheet=getSampleStyleSheet()

    style1 = stylesheet['Normal']
    style2 = stylesheet['Normal']

    style1.fontSize, style2.fontSize = 17, 13
    style1.fontName, style2.fontName = 'Arial', 'Arial'

    header = u'<para align="center">Subjets List</para>'

    p1 = Paragraph(header, style1)
    w,h = p1.wrap(width, height)
    p1.drawOn(pdf, 0, height-minus)

    minus += 30

    for i in range(len(list(item_list))):
        text = u'' + str(i+1) + '. ' + list(item_list)[i]
        minus += 20
        p = Paragraph(text, style2)
        w,h = p.wrap(width, height)
        p.drawOn(pdf, 40, height-minus)

    minus += 40

    pdf.drawString(40,(height-minus), 'Your weighted average of grades: ' + str(gradesAverage))

    pdf.showPage()
    pdf.save()

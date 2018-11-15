import xlwt
import re

def createExcelFile(table):

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    grades = []
    column = 5

    for j in range(len(table)):
        for i in range(len(table[0])):
            if i == 10 and j > 0:
                ws.write(j,i,float(table[j][i]))
            elif i == 5 and j > 0 or i == 6 and j > 0 or i == 7 and j > 0:
                regex = re.sub('\d\d.\d\d.\d\d$', '', table[j][i])
                try:
                    #ws.write(j,i,float(regex))
                    ws.cell(row=i, column=j).value = float(regex)
                except:
                    ws.write(j,i,regex)
            else:
                ws.write(j,i,table[j][i])

    wb.save('raport.xls')

import xlwt

def createExcelFile(table):

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
    style1 = xlwt.easyxf('font: name Times New Roman')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    for i in range(len(table)):
        for j in range(len(table[i])):
            if i==0:
                ws.write(i, j, table[i][j], style0)
            else:
                ws.write(i, j, table[i][j], style1)

    wb.save('raport.xls')

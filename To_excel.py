import xlsxwriter
from datetime import datetime

now = datetime.now().date()
nowstring = datetime.strftime(now,'%Y%m%d')
filename = 'result.txt'

file = open(filename, 'r')
data = file.readlines()
workbook = xlsxwriter.Workbook('result.txt.xlsx')
worksheet = workbook.add_worksheet('Sheet')

row = 1
col = 0
worksheet.write(0, 0, 'Hostname')
worksheet.write(0, 1, 'memory utill')
worksheet.write(0, 2, 'cpu utill')
worksheet.write(0, 3, 'psu state')
worksheet.write(0, 4, 'temp state')
worksheet.write(0, 5, 'fan')
worksheet.write(0, 6, 'uptime')
worksheet.write(0, 7, 'alarm')
worksheet.write(0, 8, 'port_error')

for i in data:
    for j in i.split('|'):
        worksheet.write(row, col, j)
        col += 1
    col = 0
    row += 1


workbook.close()

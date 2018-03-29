'''import xlsxwriter
wk= xlsxwriter.Workbook('Demo.xlsx')
ws= wk.add_worksheet('first')
ws.write('A1','Test Data')
ws.write('A2','Test App')

ws= wk.add_worksheet('second')
ws.write('A6','wikipedia.org')
ws.write('A7','pi')
wk.close()'''

'''
import xlsxwriter
import urllib.request
from bs4 import BeautifulSoup
from pyexcel_xls import read_data
d={}

workbook= xlsxwriter.Workbook('UrlBook.xlsx')
worksheet= workbook.add_worksheet('one')
worksheet.write('A1','domain name:')
worksheet.write('C1','www.javatpoint.com')
worksheet.write('A2','url:')
worksheet.write('C2','https://www.javatpoint.com/python-tutorial')
worksheet.write('A3','keywords:')
worksheet.write('C3','Python')
worksheet.write('C4','C#')
worksheet.write('C5','Android')
worksheet.write('C6','PHP')

worksheet= workbook.add_worksheet('second')
worksheet.write('A1','wikipedia.org')
worksheet.write('A2','pi')

d= read_data('UrlBook.xlsx')

print(d['one'])
print(d['second'])

workbook.close()
'''

import xlsxwriter
import urllib.request
from bs4 import BeautifulSoup
from pyexcel_xls import read_data
d={}

workbook=xlsxwriter.Workbook("urlbook.xlsx")
worksheet1=workbook.add_worksheet("first")
worksheet1.write('A1','javatpoint.com')
worksheet1.write('A2','https://www.javatpoint.com/java-tutorial')
worksheet1.write('A3','java')
worksheet1.write('A4','SQL')
worksheet1.write('A5','C++')
worksheet2=workbook.add_worksheet("second")
worksheet2.write('A1','tutorialspoint.com')
worksheet2.write('A2','https://www.tutorialspoint.com/python/python_data_structure.htm')
worksheet2.write('A3','Python')
worksheet2.write('A4','Data')
worksheet2.write('A5','programming')
'''d=read_data("urlbook.xlsx")

print(d['one'])
print(d['second'])'''

workbook.close()

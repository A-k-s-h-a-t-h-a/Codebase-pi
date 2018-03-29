import xlsxwriter
import re
import urllib.request
from pyexcel_xls import read_data
from bs4 import BeautifulSoup
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
d=read_data("urlbook.xlsx")
print("Reading URL from excel file")
#print(d['first'])
#print(d['second'])
L1=[]
for w in d['first']:
    L1.append("".join(map(str,w)))
#print(L1)
print(L1[1])    #worksheet 1

L2=[]
for w in d['second']:
    L2.append("".join(map(str,w)))
#print(L2)
print(L2[1])    #worksheet 2

print("Now getting the data from URL")
req1=urllib.request.Request(L1[1],data=None,headers={'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X10_9_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/35.0.1916.47 Safari/537.'})
file_handle=urllib.request.urlopen(req1)
text=file_handle.read()
#print(file_handle.read())
soup=BeautifulSoup(text,"html.parser")
#print(soup.title)
#print(soup.title.string)
#Webscrapping-getting only text
for script in soup(["script","style"]):
    script.extract()
text=soup.get_text().lower()
#lines=(line.strip() for line in text.splitlines())

#print(text)
'''
for line in lines:
    List1.append(line.split())
print(List1)
'''

List1=[]
List1.append(text.lower().split())
#print(List1)
print(L1[4])
#print(List1)
print(len(List1))
print(len(List1[0]))
'''
pattern=re.compile("^[a-z]")
s=L1[3]
so=pattern.search(s)
if so:
    print(so.group())
'''

para1=re.findall(L1[2].lower(),text)
#print()
para2=re.findall(L1[3].lower(),text)
#print(b)

D2={}
if len(para1)==0:
    D2[L1[2]]=0
for w in para1:
    if w in D2:
        D2[w]+=1
    else:
        D2[w]=1
for k,v in D2.items():
    x=(v/len(List1[0])*100)
    D2[k]=float("{0:.2f}".format(x))
print(x)

workbook.close()

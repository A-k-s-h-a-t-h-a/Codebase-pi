import re
import xlsxwriter
import urllib.request
from bs4 import BeautifulSoup
from pyexcel_xls import read_data
#from html.parser import HTMLParser

d={}

workbook=xlsxwriter.Workbook("urlbook.xlsx")
worksheet1=workbook.add_worksheet("first")
worksheet1.write('A1','javatpoint.com')
worksheet1.write('A2','https://www.javatpoint.com/java-tutorial')
worksheet1.write('A3','java')
worksheet1.write('A4','sql')
worksheet1.write('A5','C++')
worksheet2=workbook.add_worksheet("second")
worksheet2.write('A1','tutorialspoint.com')
worksheet2.write('A2','https://www.tutorialspoint.com/python/python_data_structure.htm')
worksheet2.write('A3','python')
worksheet2.write('A4','data')
worksheet2.write('A5','programming')
d=read_data("urlbook.xlsx")

#print(d['first'],"\n")
#print(d['second'],"\n")

L1=[]
for w in d['first']:
    L1.append("".join(map(str,w)))
#print(L1,"\n")
#print("reading url from excel file","\n")
#print(L1[1])

L2=[]
for w in d['second']:
    L2.append("".join(map(str,w)))
#print(L2[1])

#print("\n","Now getting data from url","\n")
req= urllib.request.Request( L1[1], data=None, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }) 
file_handle= urllib.request.urlopen(req)
test= file_handle.read()
soup = BeautifulSoup(test,'html.parser')

for script in soup(["script","style"]):
    script.extract()
text = soup.get_text().lower()
#print(text)

List= text.split()
#print(List)
#print("\n",len(List),"\n")

s1occurrence1=re.findall(L1[2].lower(),text)
#print(s1occurrence1)
#print(L1[2],len(s1occurrence1))

s1occurrence2=re.findall(L1[3].lower(),text)
#print(L1[3],len(s1occurrence2))

D1={}
for w in s1occurrence1:
    if w in D1:
        D1[w]+=1
    else:
        D1[w]=1

for w in s1occurrence2:
    if w in D1:
        D1[w]+=1
    else:
        D1[w]=1

for k,v in D1.items():
    x=(v/len(List)*100)
    D1[k]=float("{0:.2f}".format(x))

print(D1)

##

req= urllib.request.Request( L2[1], data=None, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }) 
file_handle= urllib.request.urlopen(req)
test= file_handle.read()
soup = BeautifulSoup(test,'html.parser')

for script in soup(["script","style"]):
    script.extract()
text = soup.get_text().lower()
#print(text)

List= text.split()
#print("\n",len(List),"\n")

s2occurrence1=re.findall(L2[2].lower(),text)
#print(L2[2],len(s2occurrence1))

s2occurrence2=re.findall(L2[3].lower(),text)
#print(L2[3],len(s2occurrence2))

s2occurrence3=re.findall(L2[4].lower(),text)
#print(L2[4],len(s2occurrence3))

D2={}
for w in s2occurrence1:
    if w in D2:
        D2[w]+=1
    else:
        D2[w]=1

for w in s2occurrence2:
    if w in D2:
        D2[w]+=1
    else:
        D2[w]=1

for w in s2occurrence3:
    if w in D2:
        D2[w]+=1
    else:
        D2[w]=1

for k,v in D2.items():
    x=(v/len(List)*100)
    D2[k]=float("{0:.2f}".format(x))

print(D2)
workbook.close()

##

import sqlite3
con= sqlite3.connect("Project.db")

#database.execute("create table Webscraped (domain char(255) not null, url char(255) not null, keyword char(255) not null, density float not null)")

cursor= con.cursor()

cursor.execute('''insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)''',(L1[0],L1[1],L1[2],D1[L1[2]]))
cursor.execute('''insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)''',(L1[0],L1[1],L1[3],D1[L1[3]]))
cursor.execute('''insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)''',(L2[0],L2[1],L2[2],D2[L2[2]]))
cursor.execute('''insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)''',(L2[0],L2[1],L2[3],D2[L2[3]]))
cursor.execute('''insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)''',(L2[0],L2[1],L2[4],D2[L2[4]]))

#cursor.commit()
print("Getting the data from the database and storing it in an excelsheet")
c1= cursor.execute('''select * from Webscraped where domain=?''',(L1[0],))
L7= []
for row in c1:
    L7.append(row)
print(L7,"\n")

c2= cursor.execute('''select * from Webscraped where domain=?''',(L2[0],))
L8= []
for row in c2:
    L8.append(row)
print(L8)


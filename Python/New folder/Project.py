import re
import xlsxwriter
import urllib.request
import sqlite3
from bs4 import BeautifulSoup
from pyexcel_xls import read_data

d = {}

workbook = xlsxwriter.Workbook("Urlbook.xlsx")

sheet1 = workbook.add_worksheet("first")
sheet1.write('A1','javatpoint.com')
sheet1.write('A2','https://www.javatpoint.com/java-tutorial')
sheet1.write('A3','java')
sheet1.write('A4','sql')
sheet1.write('A5','tutorial')

sheet2 = workbook.add_worksheet("second")
sheet2.write('A1','tutorialspoint.com')
sheet2.write('A2','https://www.tutorialspoint.com/python/python_data_structure.htm')
sheet2.write('A3','python')
sheet2.write('A4','data')
sheet2.write('A5','programming')
#####################################

d = read_data("Urlbook.xlsx")

L1 = []
for w in d['first']:
    L1.append("".join(map(str,w)))

L2 =[]
for w in d['second']:
    L2.append("".join(map(str,w)))

print(L1,"\n")
print(L2,"\n")
print("Reading url from excel file:")
print(L1[1])
print(L2[1],"\n")
#####################################

print("Now getting data from url in first excelsheet","\n")
req = urllib.request.Request( L1[1], data=None, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
resp = urllib.request.urlopen(req)
test = resp.read()
soup = BeautifulSoup(test,'html.parser')

for script in soup(["script","style"]):
    script.extract()
text = soup.get_text().lower()
#print(text)

List1 = text.split()
print("Number of words in this website is: ",len(List1),"\n")

print("Printing the word and its count from first excelsheet:")
s1occurrence1 = re.findall(L1[2].lower(),text)
#print(L1[2],len(s1occurrence1))

s1occurrence2 = re.findall(L1[3].lower(),text)
#print(L1[3],len(s1occurrence2))

s1occurrence3 = re.findall(L1[4].lower(),text)
#print(L1[4],len(s1occurrence3),"\n")

D1 = {}
for w in s1occurrence1:
    if w in D1:
        D1[w] += 1
    else:
        D1[w] = 1

for w in s1occurrence2:
    if w in D1:
        D1[w] += 1
    else:
        D1[w] = 1

for w in s1occurrence3:
    if w in D1:
        D1[w] += 1
    else:
        D1[w] = 1

for k,v in D1.items():
    x=(v/len(List1)*100)
    D1[k]=float("{0:.2f}".format(x))

print("Printing the words and their density from first excelsheet:")
print(D1,"\n")
#####################################

print("Now getting data from url in second excelsheet","\n")
req = urllib.request.Request( L2[1], data=None, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
resp = urllib.request.urlopen(req)
test = resp.read()
soup = BeautifulSoup(test,'html.parser')

for script in soup(["script","style"]):
    script.extract()
text = soup.get_text().lower()
#print(text)

List2 = text.split()
print("Number of words in this website is: ",len(List2),"\n")

print("Printing the word and its count from second excelsheet:")
s2occurrence1 = re.findall(L2[2].lower(),text)
#print(L2[2],len(s2occurrence1))

s2occurrence2 = re.findall(L2[3].lower(),text)
#print(L2[3],len(s2occurrence2))

s2occurrence3 = re.findall(L2[4].lower(),text)
#print(L2[4],len(s2occurrence3),"\n")

D2 = {}
for w in s2occurrence1:
    if w in D2:
        D2[w] += 1
    else:
        D2[w] = 1

for w in s2occurrence2:
    if w in D2:
        D2[w] += 1
    else:
        D2[w] = 1

for w in s2occurrence3:
    if w in D2:
        D2[w] += 1
    else:
        D2[w] = 1

for k,v in D2.items():
    x=(v/len(List2)*100)
    D2[k]=float("{0:.2f}".format(x))

print("Printing the words and their density from second excelsheet:")
print(D2,"\n")

workbook.close()
#####################################

con= sqlite3.connect("Project.db")

#con.execute("create table Webscraped (domain char(40) not null, url char(255) not null, keyword char(30) not null, density float not null)")

data= con.cursor()
'''
data.execute('insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)',(L1[0], L1[1], L1[2], D1[L1[2]]))
data.execute('insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)',(L1[0], L1[1], L1[3], D1[L1[3]]))
data.execute('insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)',(L1[0], L1[1], L1[4], D1[L1[4]]))

data.execute('insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)',(L2[0], L2[1], L2[2], D2[L2[2]]))
data.execute('insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)',(L2[0], L2[1], L2[3], D2[L2[3]]))
data.execute('insert into Webscraped(domain,url,keyword,density) values(?,?,?,?)',(L2[0], L2[1], L2[4], D2[L2[4]]))

#con.commit()
'''
print("Getting the data from the database and storing it in an excelsheet")
c1= data.execute('select * from Webscraped where domain=?',(L1[0],))
M1= []
for row in c1:
    M1.append(row)
print(M1,"\n")

c2= data.execute('select * from Webscraped where domain=?',(L2[0],))
M2= []
for row in c2:
    M2.append(row)
print(M2,"\n")

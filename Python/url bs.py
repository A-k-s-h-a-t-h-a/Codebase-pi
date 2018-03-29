"""
from urllib.request import urlopen
url='https://www.javatpoint.com/java-tutorial'
file_handle=urlopen(url)
print(file_handle.read())
"""

"""
import urllib.request
url='https://www.javatpoint.com/java-tutorial'
req=urllib.request,Request(url,data=None,headers=('User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS,X10_9_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/35.0.1916.47 Safari/537.36}
f=urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
"""


import urllib.request
from bs4 import BeautifulSoup
url="https://www.javatpoint.com"
req=urllib.request.Request(url,data=None,headers={'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X10_9_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/35.0.1916.47 Safari/537.'})
file_handle=urllib.request.urlopen(req)
text=file_handle.read()
#print(file_handle.read())
soup=BeautifulSoup(text,"html.parser")
print(soup.title)

print(soup.title.string)

#Webscrapping-getting only text
for script in soup(["script","style"]):
    script.extract()
text=soup.get_text()
lines=(line.strip() for line in text.splitlines())
for line in lines:
    print(line)

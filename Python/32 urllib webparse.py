'''
import urllib.request 
from urllib.request import urlopen
link= 'http://www.jetbrains.com'
web= urlopen(link)
print(web.read())
'''

'''
import urllib.request
link= 'http://www.google.com/doodles'
ask= urllib.request.Request(link, data=None, headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X(0-9-3)) AppleWebKit/537.36(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
fool= urllib.request.urlopen(ask)
print(fool.read().decode('utf-8'))
'''

'''
import requests

url = 'http://www.ichangtou.com/#company:data_000008.html'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=head)
print(response.content)
'''

'''
import urllib.request
from bs4 import BeautifulSoup
link='https://www.javatpoint.com/'
req = urllib.request.Request( link, data=None, 
             headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' } ) 
page = urllib.request.urlopen(req)
so = BeautifulSoup(page)
print(so.title)
print(so.link)
print(so.img)
print(so.li)
print(so.title.string)
'''



import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
url= "https://www.python-course.eu/sql_python.php"
req= urllib.request.Request(url,data=None,headers={'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X10_9_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/35.0.1916.47 Safari/537.36'})
file_handle= urllib.request.urlopen(req)
text= file_handle.read()
soup = BeautifulSoup(text,'html.parser') #src
for script in soup(["script", "style"]): 
     script.extract() #prints all script tags
test = soup.get_text() #only content without tags
print(test)
#x= test.splitlines() #splits content of each tag and stores in list
#lines = (line.strip() for line in test.splitlines()) #generator object 0x....
#for line in lines:  #only content without tags
#    print(line)         #not much of a difference


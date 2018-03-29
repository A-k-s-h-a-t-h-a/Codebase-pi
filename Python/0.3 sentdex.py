'''import urllib.request
x= urllib.request.urlopen("https://www.google.com")
print(x.read())'''


'''import urllib.request
import urllib.parse

url= 'http://pythonprogramming.net'
values= {'s':'basic', 'submit':'search'}

data= urllib.parse.urlencode(values)
data= data.encode('utf-8')
req= urllib.request.Request(url, data)
resp= urllib.request.urlopen(req)
respData= resp.read()

print(respData)'''


'''import urllib.request
try:
    x= urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))'''


'''import urllib.request
try:
    url= 'https://www.google.com/search?q=test'

    headers= {}
    headers['User-Agent']= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    req= urllib.request.Request(url, headers=headers)
    resp= urllib.request.urlopen(req)
    respData= resp.read()

    saveFile= open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))'''

# import re
# pattern= re.compile("A..T")
# matchObject= pattern.match("ACGTAAT")
# if matchObject:
#     print(matchObject.group())
#     print(matchObject.start(), matchObject.end())

# import re
# pattern= re.compile("A..T")
# s="ABCTXYFT"
# searchObject= pattern.search(s)
# if(searchObject):
#     print(searchObject.group())
#     print(searchObject.start(), searchObject.end())

# import re
# s='U123-234'
# if re.search(".\d\d\d-\d\d\d",s):
#     print("Matching")
# else:
#     print("Not matching")

# import re
# s="Hello this is my number 9876987113"
# pattern= re.compile("\d{10}")
# no= pattern.search(s)
# if (no):
#     print(no.group())

# import re
# s="Avinash got 143 marks Shubam got 240 marks and Ankita got 120 marks Rahul got 100 marks"
# patternName= re.compile("[A-Z][a-z]*")
# patternMarks= re.compile("\d{1,3}")
# names= patternName.findall(s)
# marks= patternMarks.findall(s)
# print(names)
# print(marks)
# d={}
# i=0
# for n in names:
#     d[n]= marks[i]
#     i+=1
# print(d)

# import re
# s= input("Enter URL")
# pattern= re.compile("(http|https)://")
# so= pattern.search(s)
# if (so):
#     print("Correct")
# else:
#     print("Enter valid one")

# import re
# d= input("Enter date")
# pattern= re.compile("\d{1}.|/|-\d{1}.|/|-\d{3}") #don't know correct answer
# s= pattern.search(d)
# if (s):
#     print("Correct")
# else:
#     print("Enter valid one")

# import re
# fo= open("text & no.txt","r")
# pattern= re.compile("\d{1,}")
# ctr=0
# for line in fo.readlines():
#     ctr+=1
#     if pattern.search(line):
#         print(ctr)

# import re
# fo= open("text & no.txt","r")
# pattern= re.compile("\d{1,}")
# ctr=0
# l=[]

# for line in fo.read():
#     ctr += 1
#     if (pattern.findall(line)):
#         l.append(line)
# print(l)

import re
regex=re.compile("http://(.+?)/")
fileObject=open("urls.txt","r")
allLines=fileObject.readlines()
domainList=[]
for line in allLines:
    m=regex.search(line)
    if m:
        domain=m.group(1)
        if domain not in domainList:
            domainList.append(domain)
print(domainList)
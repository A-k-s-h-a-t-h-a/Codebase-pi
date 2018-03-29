fo= open("temp.txt","r")
q= fo.readlines()
print(q)
L=[]
for z in q:
    L.append(float(z))
print(L)


templist= [float(x) for x in open("temp.txt").readlines()]
print(templist)


filteredlist= [a for a in filter(lambda x:x>30,templist)]
print(filteredlist)
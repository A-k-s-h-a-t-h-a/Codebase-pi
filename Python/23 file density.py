fo= open("ignore.txt","r")
L= fo.read().split()
s= set(L)
fo.close()

fo= open("articles.txt","r")
L1= fo.read().split()
count= len(L1)
D={}

for word in L1:
    if word not in s:
        if word not in D:
            D[word]=1
        else:
            D[word]+=1
print(D)

for word in sorted(D.keys()):
    a= round((D[word]/count)*100,3)
    z= (D[word], word, a)
    print(list(z))
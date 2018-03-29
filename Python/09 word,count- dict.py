sent= input("Enter a sentence")
word= sent.split()
xyz= set(word)
abc= list(xyz)

P= {}
for w in abc:
    P[w]= word.count(w)
print(P)


x= list(P.keys())
print(x)
x.sort()
Q={}
for z in x:
    Q[z]= P[z]
    print(z, P[z])
print(Q)


for w in P:
    if P[w]>1:
        print(w, P[w])
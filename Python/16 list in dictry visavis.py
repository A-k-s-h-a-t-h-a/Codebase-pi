sent= input("Enter a sentence for list")
L= sent.split()

T={'bad':12, 'good':78, 'joke':90}
L.insert(2, T)
print(L)


nextsent= input("Enter sentence for next list")
nextL= nextsent.split()
nextL.sort()
D={'food':28, 'water':17, 'air':36}
D['']= nextL
print(D)
# d1= {'why':'end', 'what':'began', 'rather':'continue'}
# D.update(d1)
# print(D)
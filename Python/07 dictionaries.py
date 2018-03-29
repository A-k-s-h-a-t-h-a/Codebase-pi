D= {'roll no': 142, 'name': "Anurag", "age": 26}
print(D['roll no'])
D['age']= 28
print(D)

print(len(D))

D['city']= "delhi"
print(D)

D= {'Amit':47, 'Vivek': 28, 'Rahul': 67, 'Deepa': 39}

if "Rahul" in D:
    print("yes")
else:
    print("no")

del D['Rahul']
print (D)

print(D.pop('Amit'))

print(D.get('Rahul',12))
print(D.setdefault('Dinesh', 6))

D={x:x**2 for x in range(6)}
print(D)

D2= {'name': "Anurag"}
print(D.update(D2)) #returns None, doesn't update D

D= {'tale': 12, 'story': 78}
D1= {'food': 67, 'water': 90}

print(list(D.keys()))
print(list(D1.values()))

print(D1.keys())
print(D.values())

for k in D1.keys():
    print(k)

for k in D.values():
    print(k)

D.items()
print(D.items())
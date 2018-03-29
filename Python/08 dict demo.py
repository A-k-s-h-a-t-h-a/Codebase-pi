A= {}
print(A)

B= {'roll no': 89, 'name': 'Anurag', 'age': 17}
print(B)
print(B['roll no'])
B['age']= 29
print(B)

print(len(B))
B['city']= 'Mysore'
print(B)

B.clear()
print(B)

C= {'Amit': 22, 'Vivek': 90, 'Rahul':72, 'Deepa': 19}
print(C)
if 'Rahul' in C:
    print('true')
if 'Anurag' in C:
    print('true')
else:
    print('false')

del C['Rahul']
print(C)

C.pop('Deepa')
print(C)
print(C, C.pop('Amit'))

print(C.pop('Vignesh', 10))
print(C)

print(C.pop('Vivek', 0))
print(C)

E={'Fatima': 19, 'Serena': 21}
print(E)
print(E.get('Fatima', 12))
print(E.get('Palmira', 12))

print(E.setdefault('Serena', 9))
E.setdefault ('Virat', 9)
print(E)

F= {x: x**2 for x in range(6)}
print(F)

print (F.update(E))      #not showing

print(F.keys())
print(F.values())
print(list(F.keys()))
print(list(F.values()))

for k in F.keys():
    print(k)
print("Printed keys")

for v in F.values():
    print(v)
print("Printed values")

print(F.items())
print(list(F.items()))

for k, v in F.items():
    print('Present/')

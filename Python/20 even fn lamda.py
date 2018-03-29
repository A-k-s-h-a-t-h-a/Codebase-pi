L1= [1,2,3,8]
L2= [4,6,7]
L= L1+ L2
O= [x for x in filter(lambda a: a%2==0, L)]
print(O)
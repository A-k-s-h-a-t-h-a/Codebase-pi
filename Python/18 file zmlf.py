# obj= open("abcd.txt","w")
# obj.write("Highway to hell")
# obj.close()
#
# new= open("abcd.txt","r")
# s= new.read()
# print(s)
# new.close()

# old= open("abcd.txt","r")
# #q= old.read(9)
# print(old.read(9))
# print(old.seek(1))
# old.close()

# abj= open("data.txt", "w")
# abj.close()
# print(abj.name)
# print(abj.mode)
# print(abj.closed)
#
# s= "See you again"
# L= ["\nOne Republic"]
# mod= open('data.txt', 'w')
# mod.write(s)
# mod.writelines(L)
# mod.close()

# doc= open("data.txt",  'r')
# p=doc.read()
# print(p)
# print(doc.tell())
# print(doc.seek(0))


# a= [1,2,3,4,6,7]
# b= [2,2,9,0,9]
#
# c= [x for x in zip(a,b)]
# d= {x for x in zip(a,b)}
# print(c)
# print(d)
#
# e= [x for x in map(lambda pair: max(pair), zip(a,b))]
# print(e)


# nList= ["Jack","Hina","Anurag","Deepti"]
# mList= [66,78,92,27, 88]
# D= {name:mark for name, mark in zip(nList, mList)}
# print(D)
#
# def sum(a,b):
#     return a+b
# L1= [1,2,3,8]
# L2= [4,6,7]
# L= [x for x in map(sum,L1,L2)]
# print(L)
#
# def even(a):
#     if (a%2)==0:
#         return True
#     else:
#         return False
# M=[1,2,3,6,7,9,12]
# L= [b for b in filter(even, M)]
# print(L)
#
# print((lambda x:x*6)(7))
# square= (lambda z:z*z)
# cube= (lambda y:y*y*y)
# print(square(8))
# print(cube(9))
#
# N= [x for x in map(lambda a,b: a+b, L1, L2)]
# print(N)

# class simplest:
#     pass
# z= simplest()
# z.age= 10
# print(z.age)

# class point:
#     pass
# p= point()
# p.z= 30
# p.y= 20
# print(p.z, p.y)

# class emp:
#     def __init__(self):
#         print("inside constructor")
#     def dotask(a):
#         print("doing a work")
# e1= emp()
# e1.dotask()

# class top:
#     def __init__(self, c, d):
#         self.j= c
#         self.k= d
# t= top(80, 90)
# print(t.j, t.k)

# class point:
#     def __init__(self, a, b):
#         self.x= a
#         self.y= b
#     def disp(self):
#         print(self.x, self.y)
# p1= point(30, 40)
# p1.disp()

# class emp:
#     def __init__(self, a, b):
#         self.name= a
#         self.age= b
#     def disp(self):
#         print(self.name, self.age)
# e1= emp("Abcd", 32)
# e1.disp()
# e2= emp("Efgh", 28)
# e2.disp()

# class student:
#     def __init__(self, a="Abcd", b=30):
#         self.x = a
#         self.y = b
#     # def disp(self):
#     #     print(self.x, self.y)
#     def __del__(self):
#         print("This is destructor")
# s=student()
# # s.disp()
# del s

# class number:
#     def __init__(self, a):
#         self.n= a
#     def disp(self):
#         print(self.n)
#     def square(self):
#         return self.n**2
#
#     def __add__(self, other):
#         # print(other)
#         # print(self.n+ other)
#         self.n= self.n+ other
#         return number(self.n)
#
#     def __sub__(self, other):
#         self.n= self.n - other
#         return number(self.n)
#
# n= number(6)
# print(n.square())
# n.disp()
#
# n+2
# n.disp()
#
# z= n+ 4
# z.disp()
#
# n-1
# n.disp()

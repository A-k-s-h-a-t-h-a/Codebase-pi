def checkfile(filename):
    fo= open(filename, "r")
    s= fo.read()
    L= s.split()
    SS= set(L)
    L2= list(SS)
    return L2

filename= input("Enter filename")
words= checkfile(filename)
print(words)
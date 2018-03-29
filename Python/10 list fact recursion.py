def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def factlist(a, b):
    L= []
    for w in range (a, b):
        L.append(fact(w))
    return L

z=factlist(5, 8)
print(z)
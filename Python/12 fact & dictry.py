def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def factlist(a, b):
    Q={}
    for x in range(a, b):
        Q[x]= fact(x)
    return Q

z= factlist(5, 8)
print(z)
print(z[6])
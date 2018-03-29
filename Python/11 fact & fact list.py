def fact(n):
    ans=1
    for f in range(n, 1, -1):
        ans= ans*f
    return ans

L= []
def factlist(a, b):
    for w in range (a, b+1):
        L.append(fact(w))
    return L

z= factlist (5, 8)
print(z)
z=fact(5)
print(z)
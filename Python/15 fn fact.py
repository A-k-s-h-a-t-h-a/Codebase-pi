def fact(n):
    ans=1
    for f in range(n, 1, -1):
        ans= ans*f
    return ans

x= fact(9)
print(x)
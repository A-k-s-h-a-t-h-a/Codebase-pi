def first():
    print('law'*10)

print("welcome")
first()
print("goodbye")


def second():
    print('judge'*10)
    return 10

print("salute")
x= second()
print(x)


def third():
    print('order'*10)
    return (10,30)

print("welcome")
x,y= third()
print(x, y)


def greater(a,b):
    if a>b: return a
    else: return b

print("hello")
y=10
g=80
x=greater(g, y)
print(x)
files= open("Program.txt", 'w')
t= "famous five"
files.write(t)
files.close()

run= open("Program.txt",'r')
n= run.read()
l= n.upper()
print(l)
run.close()

walk= open("Program Copy.txt", 'r+')
walk.write(l)
o= walk.read()
print(o)
walk.close()
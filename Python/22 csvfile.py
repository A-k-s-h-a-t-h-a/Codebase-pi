fo = open("Book1.csv","r")
allrecords= fo.readlines()
d={}
for record in allrecords:
    field= record.split(",")
    print(field)
    rollno= field[0]
    name= field[1]
    gender= field[2]
    marks= field[3]
    d[rollno]= {"name": name, "gender": gender, "marks": marks}
ro= input("Enter roll number")
if ro in d:
    print("name:", d[ro]["name"])
    print("gender:", d[ro]["gender"])
    print("marks:", d[ro]["marks"])
else:
    print("Not present")

def check(a):
    L=[]
    for ro in d.keys():
        if int(d[ro]["marks"])>a:
            L.append(d[ro]["name"])
    return L

n= check(70)
print(n)
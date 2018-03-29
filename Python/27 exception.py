# try:
#     a=10
#     b=0
#     c=a/b
# except ZeroDivisionError:
#     print("give valid b")
# else:
#     print(c)
# finally:
#     print("process completed")

# try:
#     a=10
#     b=2
#     d=a/x
# except NameError:
#     print("change value of x")
# else:
#     print(d)
# finally:
#     print("process completed")

# try:
#     fo= open("articles.txt")
# except FileNotFoundError:
#     s=""
# else:
#     s= fo.read()
#     fo.close()
# finally:
#     print(s)

class Textreader:
    def __init__(self, fname=""):
        self.text=""
        self.dlist=[]
        self.lines=0
        self.wordcount=0
        self.word=[]
        if len(fname)>0:
            try:
                x= open(fname, 'r')
            except FileNotFoundError:
                alllines=[]
            else:
                alllines= x.readlines()
                x.close()
            templist= "".join(alllines)
            self.word= templist.split()
            self.text= " ".join(self.word)
            self.lines= len(alllines)
            self.wordcount= len(self.word)


    def display(self):
        print(self.text)

t= Textreader("articles.txt")
t.display()

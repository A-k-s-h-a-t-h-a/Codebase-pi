class Textreader:
    def __init__(self, fname=""):
        self.text=""
        self.dlist=[]
        self.lines=0
        self.wordcount=0
        self.word=[]
        if len(fname)>0:
            x= open(fname, 'r')
            alllines= x.readlines()
            # l= len(alllines)
            templist= "".join(alllines)
            self.word= templist.split()
            self.text= " ".join(self.word)
            # self.lines= l
            self.lines= len(alllines)
            self.wordcount= len(self.word)
            x.close()

    def display(self):
        print(self.text)
    def wordlist(self):
        # convert= set(self.word)
        # c= list(convert)
        self.dlist= list(set(self.word))
        return self.dlist

    def getWC(self, wordlist):
        d= {word: self.word.count(word) for word in wordlist}
        # D={}
        # for wc in wordlist:
        #     D[wc]= self.word.count(wc)
        return d


    def save(self, fname):
        self.text= " ".join(self.word)
        fo= open(fname, 'w')
        fo.write(self.text)
        fo.close()

    def replace(self, cat, dog):
        for i in range(0, len(self.word)):
            if self.word[i]== cat:
                self.word[i]= dog
        self.text="".join(self.word)

    def __iadd__(self, other):
        self.word.append(other)
        self.text= " ".join(self.word)
        self.wordcount+= 1
        return  self

t= Textreader("articles.txt")
# t.display()
# print(t.lines)
# print(t.wordcount)
# print(t.wordlist())
#
# j= t.getWC(["is", "bought","bye"])
# print(j)

t.save("ABC.txt")
print("new text file:",t.text)
t.replace("Peter", "John")
print(t.text)
t+= "lab"
print(t.text)
print(t.wordcount)
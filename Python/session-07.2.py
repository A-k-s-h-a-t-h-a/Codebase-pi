# Session 07 Lab Q2
class textReader:
    def __init__(self,fname=""):
        self.text=""
        self.lines=0
        self.words=[]
        if len(fname)>0:
            try:
                fileObject=open(fname,"r")
            except FileNotFoundError:
                allLines=[]
            else:
                allLines=fileObject.readlines()
                fileObject.close()
                
            self.lines=len(allLines)
            tmpText=" ".join(allLines)
            self.words=tmpText.split()
            self.text=" ".join(self.words)
            self.wordcount=len(self.words)
            
    def display(self):
        print(self.text)
        
textObject=textReader("article.txt")
print(textObject.text)
# If we use a filename that does not exist then we would get blank text

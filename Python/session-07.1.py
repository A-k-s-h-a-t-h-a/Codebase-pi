# Session 07 Lab Q1
try:
    fileObject=open("article.txt","r")
except FileNotFoundError:
    text=""
else:
    text=fileObject.read()
    fileObject.close()


print(text)

# If we put a filename that does not exist in the folder
# then the text would be blank
# otherwise the data from the file


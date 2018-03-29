sent= input('Enter a sentence')
words= sent.split()
print(words)
xyz= set(words)
print(xyz)
list2= list(xyz)

for w in list2:
    print(w, words.count(w))


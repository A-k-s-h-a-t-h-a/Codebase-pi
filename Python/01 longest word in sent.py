sent=input('Input a sentence')
words=sent.split()
temp= ''
for q in words:
    if len(q)>len(temp):
        temp=q
print('longest word is',temp)

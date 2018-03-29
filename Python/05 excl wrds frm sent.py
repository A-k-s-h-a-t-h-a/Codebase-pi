sent=input('Enter a sentence')
words=sent.split()
one=set(words)

exc={'we', 'here'}

after=one-exc

l=list(after)

for x in l:
    print(x,words.count(x))

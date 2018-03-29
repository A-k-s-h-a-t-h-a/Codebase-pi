sent=input('enter sentence')
exc_word={'this','and','is','not'}
l=sent.split()
length=len(l)
l1=set(l)
new_sent=l1-exc_word
l2=list(new_sent)
for w in l2:
    x=l.count(w)
    print(w,':',x)
    d=(x/length)*100
    print('density of',w,'=',d)
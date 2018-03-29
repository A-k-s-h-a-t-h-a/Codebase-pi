# import sqlite3
# test= sqlite3.connect("wctable.db")
#
# # test.execute("create table words (word text not null, count int not null)")
#
# sent= input("Enter a nice sentence")
# shabd= sent.split()
# orig= set(shabd)
# unrep= list(orig)
#
# for w in unrep:
#     counter=  shabd.count(w)
#     test.execute("insert into words (word, count) values (?,?)", (w, counter))
#
# # test.commit()
# cursor= test.execute("select word, count from words")
# print("word ", "count")
# for entry in cursor:
#     print(entry[0], entry[1])


import sqlite3
test= sqlite3.connect("wctable.db")

# test.execute("create table words (word text not null, count int not null)")

file= input("Enter the name of the file you want to open: ")
opening= open(file, 'r')
opened= opening.read()
shabdon= opened.split()
orig= set(shabdon)
unrep= list(orig)
for w in unrep:
    counter=  shabdon.count(w)
    test.execute("insert into words (word, count) values (?,?)", (w, counter))

# test.commit()
shabd= input("Enter the word whose count you want to check in the file you just opened: ")

cursor= test.execute("select count from words where word=?",(shabd,))
for entry in cursor:
    print(entry[0])

no= input("Enter the count corresponding to the words you want to check: ")

cursor= test.execute("select word from words where count=?",(no,))
for entry in cursor:
    print(entry[0])

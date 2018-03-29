# import re
# pat= re.compile("\s\d\d\d\s")
# mat= pat.search("Hello 12 cats ran after 122 dogs")
# if mat:
#     print(mat.group())
#     print(mat.span())

# import re
# pat = re.compile("\s\w\w\w\s")
# bat = pat.search("A cat  ran after 192 dogs")
# mat = pat.findall("A cat  ran after 192 dogs")
# if bat:
#     print(bat.group())
#     print(bat.span())
# if mat:
#     print(mat)

# import re
# pattern= re.compile("(\d\d)-(\d\d)-(\d\d\d\d)")
# mat= pattern.match("12-01-2018")
# try:
#     if mat:
#         pass
# except IndexError:
#     pass
# else:
#     print("Day", mat.group())

# import re
# s= input("Enter name of your file")
# fo= open(s,"r")
# c=0
# for line in fo.readlines():
#     c+=1
#     digit= re.findall("\d{1,}",line)
#     if digit:
#         print (digit,"on line number",c)

import re
def validate(no):
    q= re.search("U-1011-\d{2}-F-(CS|BT|EC)-\d{3}",no)
    if q:
        print(no,"is a valid no")
    else:
        print("roll no is not valid")

check= validate("U-1011-92-F-EU-421")

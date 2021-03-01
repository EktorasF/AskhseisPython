text = """keimeno asci"""

charlist = list(text)
length=(len(charlist))

asciilist = []
katoptrlist = []

for i in range(length):
    a=ord(charlist[i])
    asciilist.append(a)
    b=chr(128-a)
    katoptrlist.append(b)

text2 = str(katoptrlist)
text2 = text2.replace("'","")
text2 = text2.replace(",","")
text2 = text2.replace("[","")
text2 = text2.replace("]","")

backwards = text2[::-1]
print(backwards)

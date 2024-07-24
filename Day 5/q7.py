str=input()
n=input()
k=str.upper()
uff=""
for i in k:
 uff+=chr(ord(i)+n)
print(uff)
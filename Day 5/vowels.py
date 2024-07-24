#check how many vowels are there in a string
word=input()
count=0
for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
      count+=1
print(count)
#code for printing the vowels and consonants in a string

check='a,e,i,o,u'
alp="bcdfghjklmnpqrstvwxyz"
count=0
c=0
str="hello Guys"
word=i.lower()
for i in word:
   if(i in check):
      count+=1
for i in word:
   if(i in alp):
      c+=1 
print(count)    
print(c)       



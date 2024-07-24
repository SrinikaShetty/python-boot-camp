#print the unique characters in a string
str="sriniks"
#abc="abcdefghijklmnopqrstuvwxyz"
ans=""
for i in str:
    if(i not in ans):     
        ans+=i
print(ans)       
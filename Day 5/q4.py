#reverse the numbers present in string
s="helloworld1234"
empty=0
check="0123456789"
for i in s:
    if(i in check):
        empty+=int(i)
print(empty)
       
    





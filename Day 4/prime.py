p=int(input())
count=0
r=p**0.5
if p==1:
    print("not a prime")
elif p==2:
    print("prime")
for i in range(2,2*int(r)):
    if(p%2==0):
     count+=1
     break
    if(count==0):
       print("prime number")
    else:
       print("not a primme")
       


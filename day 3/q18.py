#reverse a nUMBER
n=3657
rev=""
ans=0
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n/10
ans=int(rev)
print(ans)
print(type(ans))   

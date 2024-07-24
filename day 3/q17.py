j=int(input())
sum=0
while j>0:
    r=j%10
    if r%2==0:
        sum=sum+r
    j=j//10
print(sum)

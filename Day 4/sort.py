s=list(map(int,input().split()))
count=0
for i in range(1,len(s)-1):
    if s[i]>s[i+1] and s[i]>s[i-1]:  
     count=i
if(s[-1]>s[-2] and s[-1]>count):
     count=len(s)-1
print(s[count])    
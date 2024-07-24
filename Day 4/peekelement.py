s=list(map(int,input().split()))
for i in range(1,len(s)-1):
    if s[i]>s[i+1] and s[i]>s[i-1]:  
     print(s[i],end=" ")    
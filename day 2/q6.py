#find the avg of elements present in the e1ven index
my_list=list(map(int,input().split(" ")))
sum=0
n=len(my_list)
for i in range(n):
    if(i%2==0):
        sum+=my_list[i]
print(sum/i)    
    
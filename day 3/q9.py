#find the element present in k+N index
n=int(input())
k=int(input())
my_list=list(map(int,input().split()))
length=len(my_list)
if length<k+n :
    print("error")
else:
    for i in range(0,length):
        print(my_list[k+n],end=" ")
        break
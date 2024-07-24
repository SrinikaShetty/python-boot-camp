#print the element in a particular index (cyclic rotation)
k=int(input())
my_list=list(map(int,input().split()))
length=len(my_list)
print(my_list[(k%length)])
#for 1 based index -1 will be added
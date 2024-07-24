#using for loop print 1 to 100,append 1-100 in an empty list,find sum of all the numbers in a list
my_list=list(map(int,input().split()))
for i in range(0,len(my_list),2):
  print(my_list[i])


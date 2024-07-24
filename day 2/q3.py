#you are given with a coma separated natural numbers 1-10 print only the even numbers and count the numbers
my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    if my_list[i]%2==0:
     print(my_list[i])
    

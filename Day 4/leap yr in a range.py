year=int(input())
for i in range(2000,2025):
    if( year%4 ==0 or year%4==0 and year%100==0):
     print("leap")
else:
    print("not a leap")
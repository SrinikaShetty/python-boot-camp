#print the leap year in given range
year=int(input())
if( year%4 ==0 or year%4==0 and year%100==0):
    print("leap")
else:
    print("not a leap")
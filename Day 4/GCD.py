x=int(input())
y=int(input())
while y!=0:
 x,y=y,x%y
print("gcd of 2 numbers is",x)
#lcm=(x*y)/gcd
#password verifier
#mr.x is trying to create a new password i.e insta account these r the required conditions for creating a new password
#condition1 min len is 8;max len is 15
#only @,/ is allowed in a password
#no spaces r allowed
#only alpha numerics are allowed
#you r supposed to print: if length is exactly 8 (weak)
#if length is b/w 8-12(medium)
#if length is blw 12-15(strong)
password=input("enter thr pass")
d=len(password)
if(d<8 and d>15):
 print("check the conditons")
 count=0
 string="@ /"
 for i in password:
  if i in string[0] and string[1] and string[i]!="" :
       count+=1
       break;
if(d==8):
  print(weak)
elif(d>8 and d<12):
  print(medium)
elif(d>12 and d<15):
  print(strong)

       
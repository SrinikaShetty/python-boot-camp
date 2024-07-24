apple=10
banana=24
orange=8
cost_apples=apple*15
cost_banana=banana*4
cost_orange=orange*5
total=cost_apples+cost_banana+cost_orange
print(f"the apples cost{cost_apples}, the banana cost{cost_banana},the oranges cost{cost_orange}")
print(total)
if(total>700):
  print("the shopkeeper is a cheater")
else:
   print("shopkeeper is not a cheater")
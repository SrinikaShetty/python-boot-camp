#find the duplicate number in list 
w1=list(map(int,input().split()))
w=[]
for i in w1:
    if(i not in w):
        w.append(i)
print(w)        



























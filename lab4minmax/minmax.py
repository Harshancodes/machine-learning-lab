import math
def mm(cd,td,val,l,turn):
    if cd==td:
        return l[val]
    if turn:
        return max(mm(cd+1,td,val*2,l,0),mm(cd+1,td,val*2+1,l,0))
    else:
        return min(mm(cd+1,td,val*2,l,0),mm(cd+1,td,val*2+1,l,1))
n=int(input("enter the no of leaf nodes"))
td=math.log(n,2)
print("enter leaf node values from right to left")
l=[]
for i in range(n):
    x=int(input(f'enter {i+1} node val \t'))
    l.append(x)
print(mm(0,td,0,l,0))
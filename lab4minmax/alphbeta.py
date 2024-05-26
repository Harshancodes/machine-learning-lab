import math
n=int(input("enter the no of leaf nodes"))
td=int(math.log(n,2))
print("enter leaf node values from right to left")
l=[]
for i in range(n):
    x=int(input(f'enter {i+1} node val \t'))
    l.append(x)
Mi,Ma=-1000,1000
def ab(cd,ni,maxT,A,B,l):
    if cd==td:
        return l[ni]
    if maxT:
        best=Mi
        for i in range(2):
            val=ab(cd+1,ni*2+i,False,A,B,l)
            best=max(best,val)
            A=max(A,best)
            if B<=A:
                break
        return best
    else:
        best=Ma
        for i in range(2):
            val=ab(cd+1,ni*2+i,True,A,B,l)
            best=min(best,val)
            B=min(best,B)
            if B<=A:
                break
        return best
print(ab(0,0,1,Mi,Ma,l))
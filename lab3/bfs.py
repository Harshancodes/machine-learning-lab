n=int(input("enter the number of nodes"))
# l=[100]*n #n-> [,[100,100,100,100,100],[100,100,100,100,100],[100,100,100,100,100],[100,100,100,100,100],]
# l1=[l]*n
# print(l1)
# print(l1[0][0])
# print("enter the matrix")
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             l1[i][j]=0
#             continue
#         print(f'{i} {j}')
#         l1[i][j]=int(input())
#         print(l1)
# print(l1)
matrix=[]
for i in range(n):
    l=[]
    for j in range(n):
        if i==j:
            l.append(0)
        else:
            print(f"{i} {j}")
            x=int(input())
            if x==0:
                l.append(100)
            else:
                l.append(x)
    matrix.append(l)

from collections import deque
q=deque()
ans=[]
print("enter start node")
a=int(input())
q.append(a)
while q:
    a=q.popleft()           #q=[2,2]  # ans=[]
    for i in range(n):
        if matrix[a][i]!=0 and matrix[a][i]!=100:
            if not i in q:
                q.append(i)
    ans.append(a)

print(ans)
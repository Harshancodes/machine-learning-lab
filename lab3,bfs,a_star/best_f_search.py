graph={'A':[('B',10),('C',7),('D',9)],
       'B':[('E',8),('A',10)],
        'C':[('A',7),('D',5),('E',6)],
        'D':[('A',9),('C',5),('E',2)]}
heuristics={
    'A':32,
    'B':16,
    'C':24,
    'D':12,
    'E':0
}
start='A'
goal='E'
path=[]
def bfs(start,goal,graph,heuristics,path):
    open_list=[(0,start)]
    closed_list=set()
    closed_list.add(start)
    
    while open_list:
        open_list.sort(key=lambda x:heuristics[x[1]],reverse=True)
        cost,node=open_list.pop()
        path.append(node)

        if node==goal:
            return cost,path
        
        closed_list.add(node)
        for n,n_c in graph[node]:
            if n not in closed_list:
                closed_list.add(n)
                open_list.append((n_c+cost,n))
    return None

res=bfs(start,goal,graph,heuristics,path)

if res==None:
    print("no path")
else:
    print(f'{start}-->{goal} cost={res[0]} path={res[1]}')

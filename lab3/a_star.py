graph={'A':[('B',10),('C',7),('D',9)],
       'B':[('E',8),('A',10)],
        'C':[('A',7),('D',5),('E',6)],
        'D':[('A',9),('C',5),('E',2)],
        'E':[]}
heuristics={
    'A':32,
    'B':16,
    'C':24,
    'D':12,
    'E':0
}
start='A'
goal='E'

def a(graph,heuristics,start,goal):
    o_l=[start]
    c_l=set()
    g={start:0}
    path={start:start}

    while o_l:
        o_l.sort(key = lambda x:heuristics[x]+g[x],reverse=True)
        n=o_l.pop()

        if n==goal:
            rp=[]
            while n!=path[n]:
                rp.append(n)
                n=path[n]

            rp.append(start)
            rp.reverse()
            return rp
        for nn,cost in graph[n]:
            if nn not in o_l and nn not in c_l:
                g[nn]=heuristics[nn]+cost
                o_l.append(nn)
                path[nn]=n
            else:
                if g[nn]>g[n]+cost:
                    g[nn]=g[n]+cost
                    path[nn]=n

                if nn in c_l:
                    c_l.remove(nn)
                    o_l.append(nn)

        c_l.add(n)
    print("none")
    return None
res=(a(graph,heuristics,start,goal))
print(res)
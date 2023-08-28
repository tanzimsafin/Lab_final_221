with open('input2.txt','r') as f:
    s=(f.readline().strip().split())
    vertex=int(s[0])
    edge=int(s[1])
    graph={i:[] for i in range(1,vertex+1)}
    for i in range(1,edge+1):
        s=f.readline().strip().split()
        graph[int(s[0])].append(int(s[1]))
def BFS(graph,source,visited):
    queue=[source]
    while queue:
     v=queue.pop(0)
     visited.append(v)
     for i in graph[v]:
        if i not in visited:
            queue.append(i)
    return visited
with open('output2.txt','w') as w:
    visited=[]
    a=BFS(graph,1,visited)
    for i in a:
        w.write(str(i)+' ')
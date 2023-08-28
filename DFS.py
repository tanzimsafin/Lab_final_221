with open('input1.txt','r') as f:
    s=(f.readline().strip().split())
    vertex=int(s[0])
    edge=int(s[1])
    graph={i:[] for i in range(1,vertex+1)}
    for i in range(1,edge+1):
        s=f.readline().strip().split()
        graph[int(s[0])].append(int(s[1]))
def DFS(graph,source,visited):
    visited.append(source)
    for i in graph[source]:
        if i not in visited:
            DFS(graph,i,visited)
    return visited
with open('output1.txt','w') as w:
    visited=[]
    a=DFS(graph,1,visited)
    for i in a:
        w.write(str(i)+' ')

with open('input4.txt','r') as f:
    s=f.readline().strip().split()
    vertex=int(s[0])
    edge=int(s[1])
    graph={i:[] for i in range(vertex+1)}
    for i in range(1,edge+1):
        a=f.readline().strip().split()
        graph[int(a[0])].append(int(a[1]))
def dfs(graph,stack,visited,source):
    visited.append(source)
    for i in graph[source]:
        if i  not in visited:
            dfs(graph,stack,visited,i)
    stack.append(source)
    return stack
transpose={i:[] for i in range(vertex+1)}
for i in graph:
    for j in graph[i]:
        transpose[j].append(i)
def dfs_transpose(n,vi):
     vi.append(n)
     print(n)
     for i in transpose[n]:
        if i not in vi:
            dfs(i,vi)
     return vi
def kosaraju(graph):
    stack=[]
    visited=[]
    source=0
    d=dfs(graph,stack,visited,source)
    vi=[]
    while d:
     n=d.pop()
     if n not in vi:
       dfs_transpose(n,vi)
     print(vi)
with open('output4.txt','w') as w:
 pass
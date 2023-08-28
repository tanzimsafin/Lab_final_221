with open('input3.txt','r') as f:
    s=f.readline().strip().split()
    vertex=int(s[0])
    edge=int(s[1])
    graph={i:[] for i in range(1,vertex+1)}
    for i in range(1,edge+1):
        a=f.readline().strip().split()
        graph[int(a[0])].append(int(a[1]))
def topological_sort(graph):
    indegree=[0]*(vertex+1)
    ans=[]
    for i in graph:
        for j in graph[i]:
           indegree[j]+=1
    queue=[]
    for i in range(1,len(indegree)):
        if indegree[i]==0:
            queue.append(i)
    while queue:
     a=queue.pop(0)
     ans.append(a)
     for i in graph[a]:
           indegree[i]-=1
           if indegree[i]==0:
            queue.append(i)
    return ans
with open('output3.txt','w') as w:
   b=topological_sort(graph)
   for i in b:
      w.write(str(i)+' ')

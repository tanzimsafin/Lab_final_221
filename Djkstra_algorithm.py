with open('input2.txt','r') as f:
    s=(f.readline().strip().split())
    vertex=int(s[0])
    edge=int(s[1])
    graph={i:[] for i in range(1,vertex+1)}
    for i in range(1,edge+1):
        s=f.readline().strip().split()
        graph[int(s[0])].append(int(s[1]))

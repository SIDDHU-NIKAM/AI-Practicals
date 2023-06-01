def find(graph , node):
    if graph[node]<0:
        return node
    else:
        tmp  = find(graph, graph[node])
        graph[node] = tmp
        return tmp

def union(graph, a, b, answer):
    ta = a
    tb = b
    a = find(graph, a)
    b = find(graph, b)
    if a == b:
        pass
    else :
        answer.append([ta, tb])
        if graph[a]<graph[b]:
            graph[a] = graph[a] +graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b

# edges  =  [[1,2,3], [2, 3, 2], [2, 5,1], [3, 4,4], [4,5,8],
#            [3,7,4], [4,7,5], [5, 6, 6], [7, 6, 2], [7, 8, 1],
#            [7, 9, 2], [6, 9, 1]]
# n = 9

edges  = [[1,2,1], [1, 3, 3], [2, 6, 4], [3, 6, 2], [3, 4, 1], [4, 5, 5],
          [6, 7, 2], [6, 5, 6], [7, 5, 7]]
n = 7
answer = []
edges  = sorted(edges, key = lambda edges:edges[2])
print(edges)
graph = [-1] * (n+1)

for u,v,d in edges:
    union(graph, u, v, answer)

for item in answer:    
    print(item)

def bipartite(graph, node, visited, color, c):
    visited[node] = 1
    color[node] = c
    for child in graph[node]:
        if not visited[child]:
            tmp = bipartite(graph, child, visited, color, c^1)
            if tmp == False:
                return False
        else :
            if color[node] == color[child]:
                return False 
    return True

# canot be colored 
edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
n = 5

# can be colored 
# edges = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
# n = 6


graph = {}
visited  = {}
color = {}

for i in range(1, n+1):
    graph[i] = []
    visited[i] = 0
    color[i] = None

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

temp  = bipartite(graph, 1, visited, color, 0)
print(temp)

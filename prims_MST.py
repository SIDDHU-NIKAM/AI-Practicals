from heapq import *

def prims(graph, start, parent,distance, visited):
    bag  = []
    heappush(bag, [0,start])
    distance[start] = 0
    parent[start] = -1
    while bag:
        d,n = heappop(bag)
        if not visited[n]:
            visited[n] = 1
            for cd, cn in graph[n]:
                if distance[cn] > cd and not visited[cn]:
                    parent[cn] = n
                    distance[cn] = cd
                    heappush(bag, [cd, cn])
    print(distance)
    print(parent)

edges = [[1, 2, 1], [2, 3, 4], [3, 4, 1], [4, 5, 2], [1, 5,3], [2, 5, 2], [2,4,1]]
n = 5
graph = {}
parent  = {}
distance = {}
visited = {}

for i in range(1, n+1):
    graph[i] = []
    parent[i] = None
    distance[i] = 10**8+1
    visited[i] = 0

for u,v,d in edges:
    graph[u].append([d,v])
    graph[v].append([d,u])

start = 1
prims(graph, start, parent, distance, visited)
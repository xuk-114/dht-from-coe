import heapq
def dijkstra(n,edges,s,t):
    graph = [[] for _ in range(n)]
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    pq = [(0,s)]
    visited = set()
    distances = [float('inf')] *n
    distances[s] = 0
    while pq:
        dist,node = heapq.heappop(pq)
        if node == t:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                new_dist = dist +weight
                if new_dist <distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq,(new_dist,neighbor))
    return -1
n,m,s,t = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(m)]
result =dijkstra(n,edges,s,t)
print(result)
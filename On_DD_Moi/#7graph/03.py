from collections import deque

def shortest_path():
    n, m, s, t = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * (n + 1)
    q = deque([s])
    dist[s] = 0

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    print(dist[t])

from collections import deque

def is_connected():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    q = deque([1])   # duyệt từ đỉnh 1
    visited[1] = True
    count = 1

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                q.append(v)

    print("YES" if count == n else "NO")

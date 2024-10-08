import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

connections = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

dfs_visited = [0] * (N+1)

def dfs(V):
    dfs_visited[V] = 1
    for n in connections[V]:
        if dfs_visited[n] == 0:
            dfs(n)
       
ans = 0       
for i in range(1, N+1):
    if dfs_visited[i] == 0:
        dfs(i)
        ans += 1

print(ans)
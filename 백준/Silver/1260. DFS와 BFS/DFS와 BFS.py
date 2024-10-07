N, M, V = map(int, input().split())

connections = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    connections[a][b] = connections[b][a] = 1

dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)

def dfs(V):
    dfs_visited[V] = 1
    print(V, end =' ')
    for i in range(1, N+1):
        if connections[V][i] == 1 and dfs_visited[i] == 0:
            dfs(i)
            
def bfs(V):
    queue = [V]
    bfs_visited[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end = " ")
        for i in range(1, N+1):
            if connections[V][i] == 1 and bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i] = 1
                
dfs(V)
print()
bfs(V)
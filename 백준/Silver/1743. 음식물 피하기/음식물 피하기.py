from collections import deque

def bfs(x, y):
    global trash
    que = deque()
    que.append((x, y))
    graph[x][y] = 0
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
                trash += 1
            
N, M, K = map(int, input().split())
graph = [[0 for j in range(M)] for i in range(N)]
trash = 1
result = 0

for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j)
            if trash > result: result = trash
            trash = 1
    
print(result)
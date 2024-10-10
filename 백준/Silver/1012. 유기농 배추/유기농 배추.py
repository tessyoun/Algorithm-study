import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림

def dfs(x, y):  
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    if field[x][y] == 1:
        field[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
    
    
T = int(input())

for _ in range(T):
    warm = 0
    M, N, K = map(int, input().split())
    field = [[0 for j in range(N)]for i in range(M)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
        
    
    for i in range(M+1):
        for j in range(N+1):
            if dfs(i, j):
                warm += 1
                
    print(warm)
from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
q = deque([(0, N)])
path = []
result = 0
visited[N] = N

while q:
    time, loc = q.popleft()
    
    if loc == K:
        idx = loc
        while idx != N:
            path.append(idx)
            idx = visited[idx]
        path.append(N)
        result = time
        break
        
    if loc+1 < 100001 and visited[loc+1] == -1:
        q.append((time+1, loc+1))
        visited[loc+1] = loc
        
    if loc-1 >= 0 and visited[loc-1] == -1:
        q.append((time+1, loc-1))
        visited[loc-1] = loc
        
    if loc*2 < 100001 and visited[loc*2] == -1:
        q.append((time+1, loc*2))
        visited[loc*2] = loc    
    
print(result)
print(*path[::-1])

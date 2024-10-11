from collections import deque

def seek(N):
    que = deque([(N, 0)])
    visited = set()
    while que:
        now, cnt = que.popleft()
        
        if now == K:
            return cnt
        
        if now not in visited:
            visited.add(now)        
            if now <= 0:
                que.append((now+1, cnt+1))            
            elif now > K:
                que.append((now-1, cnt+1))
            else:
                que.append((now+1, cnt+1))
                que.append((now-1, cnt+1))
                que.append((now*2, cnt+1))
            
N, K = map(int, input().split())
print(seek(N))
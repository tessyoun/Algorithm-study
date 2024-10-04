from collections import deque

T = int(input())

for _ in range(T):
    que = deque()
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    
    que = deque((ind, imp) for ind, imp in enumerate(importance))
    
    ans = 0
    while que:
        max_imp = max(importance)
        if que[0][1] == max_imp:
            cur = que.popleft()
            importance.remove(max_imp)
            ans += 1
            
            if cur[0] == M:
                print(ans)
                break
        else:
            que.append(que.popleft()) 
                   
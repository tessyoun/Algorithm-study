from collections import deque 

def josef(que, K):
    
    result = []
    
    while que:
        for i in range(K-1):
            num = que.popleft()
            que.append(num)
        
        you = que.popleft()
        result.append(you)
        
    return result
               
def print_result(N, result):
    print('<', end ="")
    
    for i in range(N):
        if i == N-1:
            print(result[i], end = ">")
        else:
            print(result[i], end = ", ")
        
        
N, K = map(int, input().split())

que = deque(list(range(1, N+1)))

result = josef(que, K)

print_result(N, result)
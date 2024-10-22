K, N = map(int, input().split())
lan = []

for _ in range(K):
    lan.append(int(input()))
    
first, last = 1, max(lan)
answer = 0

while first <= last:
    mid = (first + last) // 2
    cnt = 0
    
    for l in lan:
        cnt += (l // mid)
        
    if cnt < N:
        last = mid - 1
    elif cnt >= N:
        first = mid + 1
        answer = mid
        
print(answer)
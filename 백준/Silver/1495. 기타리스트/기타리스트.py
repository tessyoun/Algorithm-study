N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][S] = True

for song in range(1, N+1):
    for vol in range(M+1):
        if dp[song-1][vol]:
            if vol + volumes[song-1] <= M:
                dp[song][vol + volumes[song-1]] = True
            if vol - volumes[song-1] >= 0:
                dp[song][vol - volumes[song-1]] = True


answer = -1

for i in range(M, -1, -1):
    if dp[N][i]:
        answer = i
        break
    
print(answer)        
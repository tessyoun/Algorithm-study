N = int(input())
blocks = list(input())
INF = 10000000
dp = [INF] * N
dp[0] = 0

next_block = {'B': 'O', 'O': 'J', 'J': 'B'}

for i in range(N):
    current_block = blocks[i]
    next_valid_block = next_block[current_block]
    for j in range(i + 1, N):
        if blocks[j] == next_valid_block:
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

if dp[N - 1] == INF:
    print(-1)
else:
    print(dp[N - 1])

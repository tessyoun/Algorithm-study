import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
t, p = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())
    
dp = [0] * (N + 1) 

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    finish_date = i + t[i] -1
    if finish_date <= N:
        dp[finish_date] = max(dp[finish_date], dp[i-1] + p[i])
        
print(max(dp))
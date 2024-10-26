N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

# for _ in range(N):
#     a = list(map(int, input().split()))
#     board.append(a)


for i in range(N):
    for j in range(N):
        if dp[i][j] == 0 or board[i][j] == 0: 
            continue  
        # 가야하는 칸 수    
        go = board[i][j]
        # 오른쪽으로 가는 경우
        if j+go < N:
            dp[i][j+go] += dp[i][j]
        # 아래쪽으로 가는 경우
        if i+go < N:
            dp[i+go][j] += dp[i][j]   
            
print(dp[-1][-1])        
def dfs(idx, current_sum):
    global answer

    if idx == N:
        if current_sum == S:
            answer += 1
        return
    
    dfs(idx + 1, current_sum + nums[idx])
    
    dfs(idx + 1, current_sum)

N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

dfs(0, 0)

if S == 0:
    answer -= 1

print(answer)

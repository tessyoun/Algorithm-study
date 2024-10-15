from collections import Counter

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 순차적으로 출력하기 위해 정렬
count = Counter(nums)  # 숫자들의 등장 횟수를 셈

answer = []

def dfs():
    if len(answer) == M:  # 길이가 M인 조합을 완성했을 때 출력
        print(*answer)
        return
    
    for num in count:  # 등장한 각 숫자에 대해 반복
        if count[num] > 0:  # 아직 사용할 수 있는 개수가 남아 있을 때
            answer.append(num)
            count[num] -= 1  # 사용했으니 하나 줄임
            dfs()  # 재귀 호출
            count[num] += 1  # 다시 복구 (백트래킹)
            answer.pop()

dfs()

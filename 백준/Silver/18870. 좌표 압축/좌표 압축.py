N = int(input())
nums = list(map(int, input().split()))

s_nums = sorted(set(nums))
dic_nums = {s_nums[i]:i for i in range(len(s_nums))}

for i in nums:
    print(dic_nums[i], end=" ")
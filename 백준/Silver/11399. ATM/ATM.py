N = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0

for i in range(len(times)):
    total += (len(times) - i) * times[i]
    
print(total)
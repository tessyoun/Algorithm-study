N = int(input())
village = []

for i in range(N):
    v = list(map(int, input()))
    village.append(v)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(x, y):
    global town

    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if village[x][y] == 1:
        village[x][y] = 0
        town += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            find(nx, ny)
        return True
    return False

town = 0  
ans = 0  
result = []  

for i in range(N):
    for j in range(N):
        if find(i, j): 
            result.append(town)  
            ans += 1  
            town = 0  

print(ans)  
result.sort()  
for r in result:
    print(r)

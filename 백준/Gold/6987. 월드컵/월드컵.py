
from itertools import combinations

def check(round):
    global answer
    if round == 15:
        answer = 1
        for i in score_list:
            if sum(i) != 0:
                answer = 0
                break
        return    
        
    
    con1, con2 = game[round]
    for x, y in ((0,2), (1,1), (2,0)):
        if score_list[con1][x] > 0 and score_list[con2][y] > 0:
            score_list[con1][x] -= 1
            score_list[con2][y] -= 1
            check(round+1)
            score_list[con1][x] += 1
            score_list[con2][y] += 1        

result = []
game = list(combinations(range(6), 2))

for _ in range(4):
    temp = list(map(int, input().split()))
    score_list = [temp[i:i+3] for i in range(0, 16, 3)]
    answer = 0
    check(0)
    result.append(answer)
    
print(*result)


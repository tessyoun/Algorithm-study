from itertools import combinations

def check(round):
    if round == 15:
        for i in score_list:
            if sum(i) != 0:
                return False
        return True 
        
    con1, con2 = game[round]
    for x, y in ((0,2), (1,1), (2,0)):
        if score_list[con1][x] > 0 and score_list[con2][y] > 0:
            score_list[con1][x] -= 1
            score_list[con2][y] -= 1
            if check(round + 1): return True
            score_list[con1][x] += 1
            score_list[con2][y] += 1       
            
    return False 

result = []
game = list(combinations(range(6), 2))

for _ in range(4):
    temp = list(map(int, input().split()))
    score_list = [temp[i:i+3] for i in range(0, 16, 3)]
    if check(0): result.append(1)
    else: result.append(0)
    
print(*result)
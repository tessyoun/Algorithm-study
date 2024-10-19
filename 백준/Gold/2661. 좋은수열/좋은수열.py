import sys

def is_goodSeq(temp, l):
    for length in range(1, l // 2 + 1):
        if temp[-length:] == temp[-2*length:-length]:
            return False
    return True

def dfs():      
    if len(temp) > 3:
        if not is_goodSeq(temp, len(temp)): return
                  
    if len(temp) == N:
        print(*temp, sep='')
        sys.exit()
        return 
    
    for i in range(1, 4):
        if not temp or temp[-1] != i:
            temp.append(i)
            dfs()
            temp.pop()
    
N = int(input())
temp = []
dfs()
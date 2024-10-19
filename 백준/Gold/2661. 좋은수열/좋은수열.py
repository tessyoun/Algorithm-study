import sys

def is_goodSeq(temp, l):
    for i in range(l-2):
        cand = temp[i]
        for j in range(i+1, l-1):
            if temp[j] == cand and j+j-i <= l:
                if temp[i:j] == temp[j:j+j-i]: return False
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
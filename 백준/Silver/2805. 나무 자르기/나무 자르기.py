N, M = map(int, input().split())
trees = list(map(int, input().split()))

first, last = 1, max(trees)
answer = 0

while first <= last:
    bring_home = 0
    cut = (last + first) // 2
    
    for tree in trees:
        if tree > cut:
            bring_home += (tree - cut)
            
    if bring_home < M:
        last = cut - 1
    else:
        answer = cut 
        first = cut + 1
        
print(answer)
    
    
    
def is_vps(ps):
    stack = []
    
    for i in ps:
        if i == "(":
            stack.append(1)
        elif i == ")":
            if stack: stack.pop()
            else: return "NO"
            
    if stack:
        return "NO"
    else:
        return "YES"

N = int(input())

for i in range(N):
    ps = input()
    print(is_vps(ps))
def what_order(order):
    if order[:4] == "push":
        order, num = order.split()
        stack.append(num)
    
    elif order == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
    
    elif order == "size":
        print(len(stack))
        
    elif order == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
        
    elif order == "pop":
        if len(stack) == 0: print(-1)
        else: print(stack.pop())

N = int(input())
stack = []

for i in range(N):
    order = input() 
    what_order(order)  
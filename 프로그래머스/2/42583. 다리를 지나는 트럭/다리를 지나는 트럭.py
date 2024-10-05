from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    w_sum = truck_weights[0]
    crossing = deque()
    crossing.append([truck_weights[0], 0])
    i = 1
    
    while crossing:
        answer += 1

        for c in crossing:
            c[1] += 1
        
        if crossing[0][1] > bridge_length:
            w_sum -= crossing.popleft()[0]
        
        if i < len(truck_weights) and w_sum + truck_weights[i] <= weight:
            crossing.append([truck_weights[i], 1])  
            w_sum += truck_weights[i]
            i += 1
            
    return answer

def solution(n, times):
    answer = 0
    
    first, last = min(times), max(times) * n
    
    while first <= last:
        mid = (first + last) // 2 # 시간이 mid라고 한다면
        people = 0
        
        for time in times:
            people += mid // time          
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            last = mid - 1
        else:
            first = mid + 1
    
    
    return answer
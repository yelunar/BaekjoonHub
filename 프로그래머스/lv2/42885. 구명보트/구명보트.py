from collections import deque

def solution(people, limit):
    answer = 0
    peo = deque(sorted(people))
    
    while peo:
        if len(peo) == 1:
            answer += 1
            break
        if peo[0] + peo[-1] > limit:
            peo.pop()
        else:
            peo.pop()
            peo.popleft()
        answer += 1
            
    return answer

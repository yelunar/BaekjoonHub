
def solution(s):
    answer = 0
    
    if s[0] == "-":
        tmp = int(s[1:])
        answer = -tmp
    else:
        answer = int(s)   
    
    
    return answer
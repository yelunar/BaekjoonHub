"""
p 개수랑 y 개수 비교해서 같으면 t, 다르면 f
하나도 없으면 t
"""

def solution(s):
    answer = True
    p_cnt, y_cnt = 0, 0
    
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            p_cnt += 1
        elif s[i] == "y" or s[i] == "Y":
            y_cnt += 1
        else:
            pass

    
    if p_cnt != y_cnt:
        answer = False
    
        
    return answer
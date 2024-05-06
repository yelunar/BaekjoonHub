"""
 signs -> 정수 부호 담음
 참이면 양수, 거짓이면 음수
"""

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
            if signs[i]: # 참이면, 양수
                answer += absolutes[i]
            else:
                answer -= absolutes[i]  
    
    return answer
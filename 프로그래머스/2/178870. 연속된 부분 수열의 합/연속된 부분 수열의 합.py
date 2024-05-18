"""
k: 부분 수열의 합
길이가 짧은 수열 찾기
"""

def solution(sequence, k):
    answer = []
    pointer, cnt = 0, 0
    
    for num in range(len(sequence)):
        while pointer < len(sequence) and cnt < k:
            cnt += sequence[pointer]
            pointer += 1
        
        if cnt == k:
            if not answer:
                answer = [num, pointer-1]
            else:
                if answer[1] - answer[0] > pointer-1-num:
                    answer = [num, pointer-1]
        
        cnt -= sequence[num]
    
    return answer
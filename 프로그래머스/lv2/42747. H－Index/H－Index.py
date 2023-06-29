# 논문의 인용 횟수를 담은 배열 citations
# 논문 n편 중 h번 이상 인용된 논문에 h편 이상이고 나머지 논문이 h 번 이하

def solution(citations):
    
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
        
    return 0
# 논문의 인용 횟수를 담은 배열 citations
# 논문 n편 중 h번 이상 인용된 논문에 h편 이상이고 나머지 논문이 h 번 이하

def solution(citations):
    books = len(citations)
    citations.sort()
    
    for i in range(len(citations) - 1):
        if citations[i] >= books-i:
            return books-i
        
    return 0
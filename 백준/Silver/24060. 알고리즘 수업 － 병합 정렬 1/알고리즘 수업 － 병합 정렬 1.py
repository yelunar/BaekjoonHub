# 배열 A에 K 번째 저장 되는 수를 출력/저장 횟수가 K 보다 작으면 -1을 출력

def merge_sort(LIST):
    if len(LIST) == 1:  # 원소 1이면 그대로 리턴
        return LIST
    
    mid = (len(LIST)+1) // 2
    
    Left = merge_sort(LIST[:mid]);  # 앞쪽 반 정렬
    Right = merge_sort(LIST[mid:]);  # 뒤쪽  정렬
    
    i = 0
    j = 0
    mer = []
    
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            mer.append(Left[i])
            answer.append(Left[i])
            i += 1
        else:
            mer.append(Right[j])
            answer.append(Right[j])
            j += 1
    
    while i < len(Left):
        mer.append(Left[i])
        answer.append(Left[i])
        i += 1
    
    while j < len(Right):
        mer.append(Right[j])
        answer.append(Right[j])
        j += 1
        
    return mer
    
import sys
input = sys.stdin.readline
 
N, K = map(int, input().split()) # 배열크기 n / 저장횟수 k
LIST = list(map(int, input().split()))
 
answer = []
merge_sort(LIST)
 
if len(answer) < K:
    print(-1)
else:
    print(answer[K-1])
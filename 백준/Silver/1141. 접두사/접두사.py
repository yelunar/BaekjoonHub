"""
접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합
접두사X 집합인 부분집합의 최대 크기
"""

N = int(input()) # 단어 개수
arr = [input() for _ in range(N)]
arr.sort(key=len) # 이렇게 하면 길이 오름차순으로 정렬되네 ..
cnt = 0

for i in range(N):
    flag = False
    for j in range(i + 1, N): # 현재 단어보다 길이가 긴 단어를 확인       
        if arr[i] == arr[j][0:len(arr[i])]: # 현재 단어가 접두사인지 확인
            flag = True
            break  
    
    if not flag: # 현재 단어가 접두사가 아니라면 +1
        cnt += 1

print(cnt)
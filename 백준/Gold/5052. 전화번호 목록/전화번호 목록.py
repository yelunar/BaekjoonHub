"""
전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야

** 파이썬 문자형 숫자 정렬 **
정렬 기준이 '숫자의 크기' 가 아니라 '숫자의 순서' !!

"""

for _ in range(int(input().rstrip())): # tc만큼 돌리기
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    arr.sort()

    ans = True
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
        # if arr[i+1].startswith(arr[i]):
            ans = False
            break
    
    if ans:
        print('YES')
    else:
        print('NO')
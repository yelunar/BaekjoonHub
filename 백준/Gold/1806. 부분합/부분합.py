import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
투 포인터: 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리

10 15
5 1 3 5 10 7 4 9 2 8
"""
n, s = map(int, input().split()) # n 수열길이 / 합이 s 이상 되는 것
arr = list(map(int, input().split()))

cnt = arr[0] # 합
left, right = 0, 0  # 투 포인터
min_leng = sys.maxsize # 일단 최대값 넣음

while True:
    if cnt >= s: # 조건 만족하면
        min_leng = min(min_leng, right - left+1) # 길이 반환
        cnt -= arr[left] # 위치 옮길려고 빼줌
        left += 1

    else:
        right += 1
        if right == n:
            break
        cnt += arr[right]

print(0) if min_leng == sys.maxsize else print(min_leng)

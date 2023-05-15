import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
<투 포인터>
산성 용액은 양수, 알칼리 용액은 음수
산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 
이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램
"""
n = int(input()) # 용액의 수
arr = list(map(int, input().split())) # 오름차순으로 입력

left, right = 0, n-1
ans = sys.maxsize # 특성 값
left_idx, right_idx = 0, 0

while left < right:
    tmp = arr[left] + arr[right]

    if abs(tmp) < ans:
        left_idx = left
        right_idx = right
        ans = abs(tmp)
    
    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        break

print(arr[left_idx], arr[right_idx])
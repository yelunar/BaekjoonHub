import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
<투 포인터>
연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램
"""
n, s = map(int, input().split()) # 길이 N짜리 수열, 합이 S 이상
arr = list(map(int, input().split()))

left, right = 0, 0 # 처음 포인터는 둘다 0에서 시작
ans_length = sys.maxsize
ans = 0 # 합을 저장할 변수

while True:
    if ans >= s:
        ans_length = min(ans_length, right-left)
        ans -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        ans += arr[right]
        right += 1

if ans_length == sys.maxsize:
    print(0)
else:
    print(ans_length)
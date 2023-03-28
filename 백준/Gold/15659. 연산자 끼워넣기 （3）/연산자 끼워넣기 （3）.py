import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
연산자 우선 순위는 ×와 ÷가 +와 -보다 앞선다
eval 함수 사용!
-> 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
"""

def backtracking(depth, ans, visited):
    global add, sub, mul, div, max_ans, min_ans, arr

    if depth == N:
        max_ans = max(max_ans, eval(ans))
        min_ans = min(min_ans, eval(ans))

    if add > visited[0]: 
        visited[0] += 1
        backtracking(depth+ 1, ans + '+'+str(arr[depth]), visited)
        visited[0] -= 1 # 초기화

    if sub > visited[1]:
        visited[1] += 1
        backtracking(depth+ 1, ans + '-'+str(arr[depth]), visited)
        visited[1] -= 1


    if mul > visited[2]:
        visited[2] += 1
        backtracking(depth+ 1, ans + '*'+str(arr[depth]), visited)
        visited[2] -= 1

    if div> visited[3]:
        visited[3] += 1
        backtracking(depth+ 1, ans + '//'+str(arr[depth]), visited)
        visited[3] -= 1


N = int(input()) # 숫자 개수
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 덧셈 뺄셈 곱셈 나눗셈
min_ans = 1e9
max_ans = -1e9

backtracking(1, str(arr[0]), [0, 0, 0, 0])
print(max_ans)
print(min_ans)
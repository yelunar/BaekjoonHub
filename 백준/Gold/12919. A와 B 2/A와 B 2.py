import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""
<S를 T로 바꾸는 게임>이지만 T를 S로 바꿈
문자열의 뒤에 A를 추가한다.
문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
"""

s = input().rstrip()
t = input().rstrip()
ans = 0

def check(t):
    global ans

    if t == s:
        ans = 1
        return
    if len(t) == 0:
        return
    if t[-1] == "A": # 마지막이 A이면 제거
        check(t[:-1])
    if t[0] == "B":  # 처음이 B이면 
        check(t[1:][::-1]) # 뒤집기

check(t)
print(ans)

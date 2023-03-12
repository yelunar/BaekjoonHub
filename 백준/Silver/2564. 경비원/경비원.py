import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
# 1 북 2 남 3 서 4 동
w, h = map(int, input().split()) # 가로w 세로h
N = int(input())

def go_zero(d, l):
    if d == 1:
        return l
    if d == 2:
        return 2*w+h-l
    if d == 3:
        return 2*w+2*h-l
    if d == 4:
        return w+l

arr = []
for _ in range(N+1):
    d, l = map(int, input().split())
    arr.append(go_zero(d, l))
cnt = 0

for i in range(N):
    short = abs(arr[-1] - arr[i])
    long_l = 2*(w+h) - short
    cnt += min(short, long_l)
print(cnt)
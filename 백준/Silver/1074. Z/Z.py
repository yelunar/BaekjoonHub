import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
2^N × 2^N인 2차원 배열을 Z모양으로 탐색
r행 c열을 몇 번째로 방문했는지 출력
"""

def search(x, y, N):
    global cnt
    if x == r and y == c:
        print(cnt)
        exit(0)
    if N == 1:
        cnt += 1
        return
    # 탐색 중인 배열 중에 찾는 좌표가 없으면 좌표에 크기를 더하기
    if not (x <= r < x+N and y <= c < y+N):
        cnt += N*N
        return
# 2사분면 -> 1사분면 -> 3사분면 -> 4사분면 순서로 재귀돌리기
    search(x, y, N//2)
    search(x, y+N/2, N//2)
    search(x+N//2, y, N//2)
    search(x+N//2, y+N//2, N//2)

N, r, c = map(int, input().split())
cnt = 0
search(0, 0, 2**N) # 2^n을 0, 0부터 탐색
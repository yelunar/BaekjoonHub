import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

"""
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
ans => 
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력
둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력
"""
from collections import deque

n, k = map(int, input().split())  # 수빈이는 현재 점 N / 동생은 점 K(0 ≤ K ≤ 100,000)
visited = [-1 for _ in range(100001)]
visited[n] = 0

queue = deque()
queue.append(n)

cnt = 0
while queue:
    start = queue.popleft()
    if start == k:
        cnt += 1

    for next in [start-1, start*2, start+1]:
        if 0 <= next < 100001:
            # 첫방문 혹은 방문 시간이 같은 경우가 이미 있음(가장 빠른 시간 방법의 수를 위해)
            if visited[next] == -1 or visited[next] >= visited[start] + 1:
                visited[next] = visited[start] + 1
                queue.append(next)

print(visited[k])
print(cnt)

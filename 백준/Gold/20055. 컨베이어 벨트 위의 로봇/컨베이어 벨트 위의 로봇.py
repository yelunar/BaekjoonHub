import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""
from collections import deque


n, k = map(int, input().split()) # k-> 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
arr = deque(map(int, input().split())) 
# [1, 2, 1, 2, 1, 2]
cnt = 0 # 내구도 0인 칸 개수
robot = deque([0]*n)

while True:
    cnt += 1
    arr.rotate(1)
    robot[-1] = 0
    # (1) 컨베이어 벨트 회전
    robot.rotate(1)
    robot[-1] = 0 # 내리는 위치 도달시 즉시 내림

    # (2) 로봇이동 이동하려는 칸에 로봇 없고 내구도 1이상이여야함
    for i in range(n-2, -1, -1):
        if arr[i+1] >=1 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            arr[i+1] -=1
    
    robot[-1] = 0 # 내리는 위치 도달시 즉시 내림

    # (3) 올리는 위치에 내구도 0 아니면 로봇 올리고 내구도 -1
    if arr[0] != 0 and robot[0] != 1:
        robot[0] = 1
        arr[0] -=1
    
    # (4) 내구도 0 이상인 칸수 k 이상이면 종료
    if arr.count(0) >= k:
        break
print(cnt)
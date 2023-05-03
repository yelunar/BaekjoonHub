import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""

n = int(input()) # 센서 개수
k = int(input()) # 집중국 개수
sensor = list(map(int, input().split()))
sensor.sort() # [3, 6, 7, 8, 10, 12, 14, 15, 18, 20]

answer = []
for i in range(n-1):
    answer.append(sensor[i+1] - sensor[i])

answer.sort()
print(sum(answer[:n-k]))
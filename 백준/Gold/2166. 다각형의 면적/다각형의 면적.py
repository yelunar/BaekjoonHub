import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
<정다각형 넓이 공식>
면적 = 1/2 x 둘레길이 x 변심거리
둘레길이 = 모든 변의 총 길이
변심거리 = 각 변의 중심으로부터 수직으로 뻗어 나가 다각형의 중심으로 모이는 선분
"""

n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

xx, yy = 0, 0
for i in range(n):
    xx += x[i] * y[i+1]
    yy += y[i] * x[i+1]

print(round(abs((xx-yy)/2),1))
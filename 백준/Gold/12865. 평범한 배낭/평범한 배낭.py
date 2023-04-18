import sys 
#sys.stdin = open('input3.txt')
input = sys.stdin.readline

"""
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력
"""

n, k = map(int, input().split()) # 최대 K만큼의 무게만
dp = [[0]*(k+1) for _ in range(n+1)]
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split()))) #무게 W와 가치 V

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = arr[i][0]
        value = arr[i][1]
        if j < weight: # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])
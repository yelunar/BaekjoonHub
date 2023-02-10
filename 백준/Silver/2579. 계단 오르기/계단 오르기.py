# 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻음
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있음
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함x
# 마지막 도착 계단은 반드시 밟아야 함

# 총 점수의 최댓값을 구하기

n = int(input()) # 계단 개수
stairs = []

for i in range(n):
    scores = int(input())
    stairs.append(scores)
    
# stairs [10, 20, 15, 25, 10, 20]

dp = [0] * n

if len(stairs) <= 2:
    print(sum(stairs))

else:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + stairs[0]

    for i in range(2, n):

        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    
    print(dp[-1])
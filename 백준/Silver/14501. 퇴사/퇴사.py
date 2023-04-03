import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

"""
 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담
 dp[i]는 i번째날까지 일을 했을 때, 최대값을 보관
 역순으로 진행

"""

N = int(input())
T, P = [0 for i in range(N+1)], [0 for i in range(N+1)] # 각각 빈 리스트 할당
for i in range(N):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

# dp[i]는 i번째날까지 일을 했을 때, 최대값
dp = [0 for i in range(N+1)] # 일단 값 저장할 빈 리스트 선언

for i in range(len(T)-2, -1, -1) : # 역순으로 ㄱㄱ
    if T[i] + i <= N: # 날짜 초과 하지 않은 경우
        dp[i] = max(P[i] + dp[T[i] + i], dp[i+1])
    else:
        dp[i] = dp[i+1] # i 번째에서 날짜를 초과하면 i+1 번째 값을 복사해줘야함
print(dp[0])
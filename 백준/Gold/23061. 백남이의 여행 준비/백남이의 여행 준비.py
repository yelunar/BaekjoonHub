import sys 
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

"""
한 줄에 가장 효율적으로 짐을 싸기 위해 필요한 가방의 번호를 출력
가방은 한 개만 선택할 수 있으며, 최적의 가방이 여러 가지라면 그중 가장 작은 번호를 출력
"""

n, m = map(int, input().split()) # N 물건의 종류 M 가방 수 
arr = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

bags =[0]+[int(input()) for _ in range(m)] # [0, 20, 21, 22]
dp = [[0]*(max(bags)+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(max(bags)+1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j])  # 위에 값 그대로 가져오기
        if j - arr[i][0] >= 0: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i][j], dp[i - 1][j - arr[i][0]] + arr[i][1])

######################################################  최소공배수 구하기
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
def lcm(a, b):
    return a * b // gcd(a, b)

ans = 1
for i in range(2, m+1):
    LCM = lcm(bags[ans], bags[i])
    value1 = dp[n][bags[ans]] * LCM // bags[ans]
    value2 = dp[n][bags[i]] * LCM // bags[i]
    if value2 > value1: ans = i

print(ans)

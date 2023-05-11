import sys
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

"""
왜 DP?
어떤 문자열이 팰린드롬인지 확인하려면, 
양 끝의 문자가 같은지를 확인하고 양 끝단을 제외한 문자열이 팰린드롬인지 확인하면 됨

양 끝의 문자가 다르면 -> 팰린드롬 아님
양 끝의 문자가 같을 때, 가운데 문자열이
- 팰린드롬이라면 -> 팰린드롬
- 팰린드롬이 아니라면 -> 팰린드롬 아님
가운데 문자열이 팰린드롬인지 아닌지 모른다면 알 때까지 문자열의 길이를 앞뒤로 하나씩 줄이면서 위 과정 반복
"""
n = int(input())  # 수열크기
board = list(map(int, input().split()))  # 칠판에 적은 수
dp = [[0] * n for _ in range(n)]

for i in range(n):  # 검사하는 길이 1일때
    dp[i][i] = 1

for i in range(n-1):  # 검사하는 길이 2일 때
    if board[i] == board[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):  # 검사하는 길이 3이상일때
    for j in range(n-i):
        if board[j] == board[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

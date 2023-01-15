n = int(input()) #명수
m = list(map(int,input().split()))
answer = 0

m.sort()
for i in range (1, n+1):
    answer += sum(m[0:i])
print(answer)
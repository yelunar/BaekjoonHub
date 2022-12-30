n = int(input())
score = list(map(int, input().split()))
max = max(score)

for i in range (n):
    score[i] = score[i]/max*100

print(sum(score)/n)
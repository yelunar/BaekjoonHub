A = []
B = []

N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]


for i in range(N):
    for j in range(M):
        for k in range(K):
            result[i][k] += A[i][j] * B[j][k]

for i in result:
    print(*i)
from sys import stdin

N = stdin.readline()
A = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())
cnt = 0

for i in range(len(A)):
    if A[i] >= B:
        A[i] -= B
        cnt += 1

        if A[i] % C == 0:
            cnt += (A[i] // C)
        else:
            cnt += (A[i] // C) + 1
    else:
        cnt += 1

print(cnt)
N, K = map(int, input().split()) # 온도, 측정한 전체 날짜 수
arr = list(map(int, input().split()))

prefix_sum = [0]*(N+1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

tmp = []

for i in range(N-K+1):
    tmp.append(prefix_sum[i+K]-prefix_sum[i])

print(max(tmp))
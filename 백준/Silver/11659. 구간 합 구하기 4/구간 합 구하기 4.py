"""
<구간 합 구하기 4>
배열에서 구간의 합을 구할 때 
배열과 구간의 크기가 모두 크다면,

배열의 구간에서 원소를 일일이 훑으며 더해주는 것은 
시간 복잡도가 O(N2)에 가깝게 되므로 성능이 매우 좋지 않다.

따라서 입력 받은 배열을 누적 합 배열로 바꾸고,

구하려 하는 구간 i, j에 해당하는 두 원소의 차를 구해 
그 구간의 합을 구하는 방식을 사용
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 숫자 개수 합구해야하는 횟수
data = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + data[i] # prefix_sum[i+1] - prefix_sum[i] = lst[i]

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])
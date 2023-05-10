import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.
한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 
한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다.

ans => 필요한 최소 강의실의 수
"""

# 반복문을 돌면서 arr[i] 수업이 heap에 저장된 가장 일찍 끝나는 수업보다 늦게 시작하면, 
# 수업시간이 겹치지 않는다 => heap.pop() (왜냐면 같은 교실에서 수업해서)

from heapq import heappop, heappush

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] # 강의 번호, 강의 시작 시간, 강의 종료 시간
arr.sort(key=lambda x:x[1]) # 강의 시작 시간을 기준으로 정렬
heap = []
cnt = 0

# 다른 수업 시간과 겹치지 않으면 이전 수업 pop
for study in arr:
    while heap and heap[0] <= study[1]:
        heappop(heap)
    heappush(heap, study[2])
    cnt = max(cnt, len(heap))
    # print(heap)

print(cnt)

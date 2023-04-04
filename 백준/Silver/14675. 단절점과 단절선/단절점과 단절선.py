import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

"""
단절점: 정점을 제거하였을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우
단절선: 해당 간선을 제거하였을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우

 t가 1일 때는 k번 정점이 단절점인지에 대한 질의, 
 t가 2일 때는 입력에서 주어지는 k번째 간선이 단절선인지
"""


N = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
 
q = int(input())

for _ in range(q):
    t, k = map(int,input().split())
    if t == 2:
        print("yes")
    else:
        if len(arr[k]) <= 1:
            print("no")
        else:
            print("yes")
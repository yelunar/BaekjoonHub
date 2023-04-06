import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""

"""

def find_parent(me):
    parent_list = [me]
    while parent[me]:
        parent_list.append(parent[me])
        me = parent[me]
    return parent_list

for _ in range(int(input())):
    N = int(input())
    parent = [0] * (N + 1) # 노드 정보 저장

    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a
    x, y = map(int, input().split())
    x_parent = find_parent(x) # [3, 2]
    y_parent = find_parent(y) # [5, 1, 3, 2]

    
    # len 맞춰줘야함 아니면 어케하는지 모름 
    i, j = 0, 0
    if len(x_parent) > len(y_parent):
        i = len(x_parent) - len(y_parent)
    else:
        j = len(y_parent) - len(x_parent)

    # 같은 깊이에서 최소 공통 조상 찾기
    while x_parent[i] != y_parent[j]:
        i += 1
        j += 1
    print(x_parent[i])
import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
union-find -> 그래프 알고리즘으로 두 노드가 같은 그래프에 속하는지 판별
노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산으로 이루어짐
"""
# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x: # 자기 자신이 루트 노드이면 ㅌ 반환
        parent[x] = find(parent[x]) # 부모 테이블 갱신
    return parent[x] # 루트노드 반환

#---------------------------------------------------------- (2)

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b:  # a와 b의 루트 노드가 다르면 두 집합을 합치기
        parent[b] = a
    else:
        parent[a] = b

#---------------------------------------------------------- (1)

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i
#---------------------------------------------------------- (3)

# Union 연산을 각각 수행
for _ in range(m):
    action, a, b = map(int, input().split())
    if action == 0: # 원소가 포함되어 있는 집합을 합치기
        union(a, b)
    else:  # 두 원소가 동일한 집합인지 판단
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
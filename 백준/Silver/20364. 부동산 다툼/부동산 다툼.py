import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

"""
이진 트리 모양의 땅
루트 땅의 번호는 1

이진트리의 특성을 이해해야해!!
"""

def visit(a):
    ans = 0
    b = a
    while b > 0:
        if b in visited:
            ans = b
        b//=2 # 부모 노드는 자식을 2로 나눈 값
    if ans == 0:
        visited.add(a)
    print(ans)

# ---------------------------------------------------

n,q = map(int,input().split()) # 땅 개수 N 오리 수 Q
num = []
visited = set()

for _ in range(q): # 정보 일단 넣어줌
    a = int(input())
    num.append(a)
    
for i in num:
    visit(i)
import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
"""
 첫 번째 빈 칸에는 A를, 두 번째 빈 칸에는 B를 넣었을 때 답을 구하라
 완전 이진 트리
 M(A, B) = k
 1~ A, 1~B까지 가는데 노드 최대값 
a // 2
 문제를 해석하면 결국 두 노드의 가장 가까운 부모 노드를 찾는 것이다.
 부모 노드는 자식 노드에서 2로 나눈 값
 두 노드의 부모 노드가 같을 때까지 반복하여 두 노드의 가장 가까운 부모 노드를 찾는다.

10도 곱해줘야함
"""
T = int(input()) # tc
for tc in range(T):
    A, B = map(int, input().split())
    a_lst = []
    b_lst = []

    while True:
        if A==B:
           print(A*10)
           break
        if A > B:
           A //= 2

        else:
           B //= 2
# 오큰수 -> 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
# 그러한 수가 없는 경우에 오큰수는 -1
# index 0 부터 a1임

import sys 

A = int(input()) # 수열 A 크기
numbers = list(map(int, sys.stdin.readline().split()))

NGE = [-1 for _ in range(A)] # 미리 -1 할당해 시간초과 해결
stack = []

stack.append(0)
i = 1

while stack and i < A: # 스택 안에 값 있고 i가 A 보다 작을떄
    while stack and numbers[stack[-1]] < numbers[i]:
        # 스택 값 있고 스택 제일 위 인덱스가 i 보다 크면
        NGE[stack[-1]] = numbers[i] # 값 추가
        stack.pop()
    
    stack.append(i)
    i += 1

print(*NGE)

"""
시간초과 나서 다시품

시간복잡도 O(N^2) 였던 for 문 X 2 와 달리, 
for 문안에 스택이 들어있는 것은 시간복잡도가 O(N)이다.

스택 -> 왼쪽에서 오른쪽 혹은 오른쪽에서 왼쪽으로 순차적으로 방향성을 갖고 있음
조건을 만족하지 않으면 "저장"되었다가 나중에라도 체크해야한다.
 -> 스택의 구조는 "쌓인다"라는 특징

"""
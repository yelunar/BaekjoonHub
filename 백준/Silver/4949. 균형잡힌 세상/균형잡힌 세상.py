# 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램짜기
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호 존재
while True:
    n = input()
    stack = []

    if n == '.':
        break

# 시작괄호면 stack에 쌓아두고 
# 끝괄호 나오면 하나씩 pop하여 리스트에서 제거

    for i in n:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
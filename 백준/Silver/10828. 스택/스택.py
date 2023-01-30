import sys
n = int(sys.stdin.readline()) # test case 
stack = []

for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push': # 정수 X를 스택에 넣음
        stack.append(int(order[1]))
    
    elif order[0] == 'pop':
        if len(stack)==0: 
            print(-1) # 정수가 없는 경우에는 -1을 출력
        else:
            print(stack.pop()) # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
        
    elif order[0] == 'size': #  정수의 개수를 출력
        print(len(stack))
    
    elif order[0] == 'empty': # 스택이 비어있으면 1, 아니면 0을 출력
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == 'top': # 스택의 가장 위에 있는 정수를 출력
        if len(stack) == 0: # 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
        else:
            print(stack[-1])
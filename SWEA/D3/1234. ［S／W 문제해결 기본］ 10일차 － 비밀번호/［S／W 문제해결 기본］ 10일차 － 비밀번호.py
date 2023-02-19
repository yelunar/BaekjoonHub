T = 10
for tc in range(1, T+1):
    N, numbers = map(str, input().split())
    N = int(N)
    stack = []
    num_list = []

    for num in numbers:
        num_list.append(num)
    
    for num in numbers:
        if not stack:
            stack.append(num)
        else:
            if stack[-1] != num:
                stack.append(num)
            else:
                stack.pop()
    
    result = ''
    for i in stack:
        result += i
        
    print(f'#{tc} {result}')
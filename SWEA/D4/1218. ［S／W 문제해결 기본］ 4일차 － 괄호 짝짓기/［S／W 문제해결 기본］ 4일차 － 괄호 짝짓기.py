T = 10
for tc in range(1, T+1):
    length = int(input())
    words = input()
    stack = []
    result = 1

    for word in words:
        if word =='<' or word == '(' or word =='{' or word == '[':
            stack.append(word)
        else:
            if word == '>':
                if '<' in stack:
                    a = stack.index('<')
                    stack.pop(a)
                else:
                    stack.append(word)
            elif word == ']':
                if '[' in stack:
                    a = stack.index('[')
                    stack.pop(a)
                else:
                    stack.append(word)
            elif word == ')':
                if '(' in stack:
                    a = stack.index('(')
                    stack.pop(a)
                else:
                    stack.append(word)
            elif word == '}':
                if '{' in stack:
                    a = stack.index('{')
                    stack.pop(a)
                else:
                    stack.append(word)

    if stack:
        result = 0

    print(f'#{tc} {result}')
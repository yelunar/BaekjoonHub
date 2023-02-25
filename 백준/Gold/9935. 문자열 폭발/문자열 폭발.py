words = input()
bomb = list(input())
stack = []

for i in words:
    stack.append(i)
    if stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
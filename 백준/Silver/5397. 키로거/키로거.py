# 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
# 강산이가 입력한 순서대로 길이가 L인 문자열
# 강산이가 백스페이스를 입력했다면, '-'가 주어짐
# 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지움
#  화살표의 입력은 '<'와 '>'로 주어진다. 
#  이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직임

T = int(input()) # tc

for _ in range(T): # tc만큼 반복
    word = input()
    left = [] # 커서 기준 왼, 오 스택 
    right = []

    for i in word:
        if i == '>':
            if right:
                left.append(right.pop())
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    
    print(''.join(left)+''.join(reversed(right)))
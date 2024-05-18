"""
같은 알파벳 두개 붙어잇는거 찾음
그 두개 제거 하고 또 붙여서 다 없앰
다 없앨 수 있으면 1, 아니면 0
"""

def solution(s):
    answer = 1
    lst = []
    
    for i in s:
        if len(lst) == 0:
            lst.append(i)
        elif lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)
    
    if lst:
        answer = 0

    return answer
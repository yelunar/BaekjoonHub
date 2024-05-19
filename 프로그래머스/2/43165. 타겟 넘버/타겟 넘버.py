def solution(numbers, target):
    answer = 0
    nodes = [0] # 가능한 모든 경우의 수 모음
    
    for num in numbers:
        tmp = []
        
        for node in nodes:
            tmp.append(node+num)
            tmp.append(node-num)

        nodes = tmp
    
    for node in nodes:
        if node == target:
            answer += 1
    
    return answer
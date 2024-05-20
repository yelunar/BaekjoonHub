def solution(array, commands):
    answer = []
    
    # [0] 부터 [1]까지 숫자 자르고 정렬해서 [2]번째에 있는 수 구하기
    
    for sequence in range(len(commands)): # commands 수 만큼 반복 ( 0 1 2 )
        tmp = []
        
        
        for item in range(commands[sequence][0]-1, commands[sequence][1]):
            tmp.append(array[item])
            
        tmp.sort()
        answer.append(tmp[commands[sequence][2]-1])
    
    return answer
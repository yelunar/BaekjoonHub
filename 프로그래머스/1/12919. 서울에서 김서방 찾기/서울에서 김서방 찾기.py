def solution(seoul):
    answer = ''
    location = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            location = i
    answer = "김서방은 " + str(location) + "에 있다"
    
    print(answer)
    
    return answer
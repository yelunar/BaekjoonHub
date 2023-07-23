"""
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
각 배포마다 몇 개의 기능이 배포되는지를 return
"""

def solution(progresses, speeds):
    answer = []   
    time, cnt = 0, 0
    
    while len(progresses) >0: # 아직 기능이 남아있으면
        if(progresses[0]+speeds[0]*time>=100):
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt >0:
                answer.append(cnt)
                cnt = 0
            time += 1
    
    answer.append(cnt)
        
    return answer
"""
 차량의 경로 routes가 매개변수로 주어질 때, 
 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지
 
routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점
"""

def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key = lambda x:x[1])
    
    for site in routes:
        start = site[0]
        if start > camera:
            answer += 1
            camera = site[1]
    
    
    return answer
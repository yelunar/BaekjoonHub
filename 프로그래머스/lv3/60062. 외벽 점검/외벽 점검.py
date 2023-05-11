"""
레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터
빠른 공사 진행을 위해 점검 시간을 1시간으로 제한
레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리
친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동

외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist
return => 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값
"""
from itertools import permutations

def solution(n, weak, dist):
    leng = len(weak)
    for x in range(leng):
        weak.append(weak[x] + n)

    answer = len(dist) + 1 # 결과값을 max로 잡아둠

    for start in range(leng): # weak 길이만큼 순회
        for friends in list(permutations(dist, len(dist))): # 친구들이 투입될 순서 순열로 변경
            cnt = 0
            # 친구들의 1시간동안 이동거리를 순열로 뽑아낸 배열의 cnt - 1 번째의 값을 빼줌
            position = weak[start] - friends[cnt - 1]
            
            for idx in range(start, start + leng):
                if position < weak[idx]:
                    cnt += 1
                    if cnt > len(dist): # 가지고 있는 친구보다 더 많이 필요하면 불가
                        break
                    position = weak[idx] + friends[cnt - 1]
            answer = min(answer, cnt)
            
    if answer > len(dist):
        return -1
    else:
        return answer
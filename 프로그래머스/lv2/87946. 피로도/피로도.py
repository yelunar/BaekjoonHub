from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons_leng = len(dungeons)
    
    for permut in permutations(dungeons, dungeons_leng):
        now = k # 남아있는 피로도
        cnt = 0
        for pm in permut:
            if now >= pm[0]:
                now -= pm[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    
    return answer
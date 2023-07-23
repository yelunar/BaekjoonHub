"""
일렬로 나열된 n개의 집에 택배를 배달
ans -> 럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리

트럭에 실을 수 있는 재활용 택배 상자의 최대 개수 cap
배달할 집의 개수 n
각 집에 배달할 재활용 택배 상자의 개수 deliveries 
각 집에서 수거할 빈 재활용 택배 상자의 개수 pickups
"""

def solution(cap, n, deliveries, pickups):
    d_val, p_val = 0, 0 # 배달한거, 수거한거
    ans = 0
    
    for i in range(n):
        d_val += deliveries[n-i-1] # 뒤에서부터 온다
        p_val += pickups[n-i-1]
        
        while d_val >0 or p_val >0:
            d_val -= cap
            p_val -= cap
            ans += 2*(n-i)
    
    return ans
N = int(input()) # 명수

data = []
rank = []

for _ in range(N):
    weight, height = map(int, input().split())
    data.append([weight, height]) # 중첩 리스트로 쌍으로 넣는다.

for i in range(N):
    cnt = 1 # 등수 매길 cnt
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    
    rank.append(cnt)

print(*rank)

# ================================================== 
# 멍청이 방법 답은 나오는데 왜 틀렸지 
"""
# 각각 rank 다 더해서 또 그걸 최종 rank로 하면 됨

N = int(input()) # 명수
weight = [] #[55, 58, 88, 60, 46]
height = [] #[185, 183, 186, 175, 155]
rank_list = []
rank = 1

for _ in range(N):
    w, h = map(int,input().split())
    weight.append(w)
    height.append(h)

for i in range(len(weight)):

    max_weight = max(weight) # 최대 값 찾고
    max_idx_1 = weight.index(max_weight)
    weight[max_idx_1] = rank
    rank += 1

rank = 1

for i in range(len(height)):

    max_height = max(height) # 최대 값 찾고
    max_idx_2 = height.index(max_height)
    height[max_idx_2] = rank
    rank += 1

for i in range(len(weight)): #어짜피 키랑 몸무게 쌍이니까 아무거나 len 하면됨

    result = weight[i] + height[i]
    rank_list.append(result)
    result = 0 # result 초기화

# rank_list -> [6, 6, 2, 6, 10]

new_rank_list = sorted(rank_list) # 순서대로 정렬해줌

answer = []

for i in rank_list:
    answer.append(new_rank_list.index(i)+1)

print(*answer)

"""
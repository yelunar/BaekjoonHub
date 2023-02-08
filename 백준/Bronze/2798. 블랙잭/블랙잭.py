import sys
from itertools import combinations

# 카드3장골라서 M이거나 M에 가까운 수의 합 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
N, M = map(int, sys.stdin.readline().split()) #카드개수, 합
cards = list(map(int, sys.stdin.readline().split())) #카드쓰진수
cards_sum = [] # 카드 합 넣을 리스트
subtract = []

for i in combinations(cards, 3):
    cards_sum.append(sum(i))
    if M-sum(i) >= 0:
        subtract.append(M-sum(i))

if 0 in subtract:
    print(M)
else:
    mini = min(subtract)
    print(M-mini)
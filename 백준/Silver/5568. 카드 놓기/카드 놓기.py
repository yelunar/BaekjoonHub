# 카드적힌 수는 1 ~ 99 까지
# k장 선택해서 가로로 나란히 정수 만들기
# k개 선택해서 만들수 있는 정수 개수

from itertools import permutations

n = int(input()) #카드 장수
k = int(input()) # 몇개 선택하는지
cards = []

for _ in range(n):
    card = input() # int형으로 받으면 안됨 
    cards.append(card) # 카드 넘버 인풋받아서 cards 리스트에 삽입

number = set()

for i in permutations(cards,k):
    number.add(''.join(i))

print(len(number))
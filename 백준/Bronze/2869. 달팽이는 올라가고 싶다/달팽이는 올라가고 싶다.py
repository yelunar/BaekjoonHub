# 달팽이는 올라가고 싶다.....
import sys
import math

#a미터오르고 b미터 미끄러지고 V미터오르고싶다
A, B, V = map(int, sys.stdin.readline().split()) 
height = (V - B) / (A - B)
print(math.ceil(height))


# 시간초과 ㅠ
# height = 0
# day = 0

# while height <= V:
#     day += 1
#     height += A
#     if height >= V:
#         break
#     height -= B

# print(day)
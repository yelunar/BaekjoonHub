import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""
 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제

 딕셔너리 정리하기 좋은 문제인듯
"""

n = int(input())  # 단어 개수
words = []
for _ in range(n):
    words.append(input().rstrip())

dict = {}
for word in words:
    digit = len(word) - 1  # 자릿수(곱해줄 10의 몇승?)
    for i in word:
        if i in dict:
            dict[i] += pow(10, digit)
        else:
            dict[i] = pow(10, digit)
        digit -= 1  # 자릿수 빼줌

dict = sorted(dict.values(), reverse=True)  # 큰값부터 정렬 / 값들만 리스트로 뺌

ans, num = 0, 9

for i in dict:  # key만 나옴
    ans += i*num
    num -= 1

print(ans)

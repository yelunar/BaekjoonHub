#첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수
#모든 원소가 빈 칸을 사이에 두고 입력
import sys

a, b = map(int, input().split())
a_data = list(map(int,sys.stdin.readline().split()))
b_data = list(map(int,sys.stdin.readline().split()))

sym_diff = list(set(a_data) ^ set(b_data))

print(len(sym_diff))
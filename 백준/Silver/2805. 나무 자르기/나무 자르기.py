import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)
"""
#  상근이는 절단기에 높이 H를 지정
 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라감
 그 다음, 한 줄에 연속해있는 나무를 모두 절단
 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것

 절단기에 설정할 수 있는 높이는 양의 정수 또는 0
 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력
"""

def binarysearch(target):
    start, end = 0, max(arr)    # 시작 위치와 끝 위치를 지정
    while start <= end: # 시작 위치가 끝 위치를 넘지 않을 때까지 반복
        mid = (start+end) // 2
        cnt = 0 # 자른 나무의 길이를 합산할 변수
        for tree in arr:
            if tree > mid:  # 현재 위치보다 높이가 높은 나무만 자를 수 있음
                cnt += tree- mid # 자른 나무의 길이를 합산
        if cnt < target: # 합산된 자른 나무의 길이가 가져가려는 길이보다 작으면
            end = mid -1  # 자를 위치를 더 위쪽으로 이동하여 나무의 길이를 더 높임
        else:
            start = mid + 1      # 자를 위치를 더 아래쪽으로 이동하여 나무의 길이를 더 낮춤
    return end  # 가져갈 수 있는 가장 긴 나무의 길이를 반환

N, M = map(int, input().split()) # 나무의 수 N과 집으로 가져가려고 하는 나무의 길이 M / 4 7
arr = list(map(int, input().split())) # 20 15 10 17
# arr.sort()

print(binarysearch(M))
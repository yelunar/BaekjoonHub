import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 
A는 결코 선발되지 않음

서류심사 성적, 면접 성적의 순위
"""
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    ans = 1
    now = arr[0][1]
    for i in range(N):
        if now > arr[i][1]:
            ans += 1
            now = arr[i][1]

    print(ans)

"""
[[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
[[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
"""
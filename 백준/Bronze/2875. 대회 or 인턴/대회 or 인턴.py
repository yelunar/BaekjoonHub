#  2명의 여학생과 1명의 남학생이 팀을 결성해서 나가는 것이 원칙
#  여학생의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K

N, M, K = map(int, input().split())
team = 0

while True:
    N -= 2
    M -= 1
    if N < 0 or M < 0 or (N+M) < K:
        break
    team += 1
print(team)
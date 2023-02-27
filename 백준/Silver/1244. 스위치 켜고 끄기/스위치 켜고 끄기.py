N = int(input())
bit = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    gender, switch = map(int, input().split())

    if gender == 1:
        for i in range(1, (len(bit) // switch) + 1):
            if bit[(switch * i) - 1] == 0:
                bit[(switch * i) - 1] = 1
            else:
                bit[(switch * i) - 1] = 0

    if gender == 2:
        if bit[(switch - 1)] == 0:
            bit[(switch - 1)] = 1
        else:
            bit[(switch - 1)] = 0
        l = switch - 2
        r = switch
        while l >= 0 and r < N and bit[l] == bit[r]:
            if bit[l] == 0:
                bit[l], bit[r] = 1, 1
            elif bit[l] == 1:
                bit[l], bit[r] = 0, 0
            l -= 1
            r += 1
            if l < 0 or r >= N:
                break

cnt = 0
ans = ''
for i in range(N):
    ans += (str(bit[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0
if len(ans) != 0:
    print(ans)

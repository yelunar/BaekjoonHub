N = int(input())
arr = []

for i in range(1, N+1):
    a = N
    b = i
    tmp = [N, i]

    while True:
        c = a - b
        if c >= 0:
            tmp.append(c)
            a = b
            b = c
        else:
            if len(tmp) > len(arr):
                arr = tmp
            break
print(len(arr))
print(*arr)
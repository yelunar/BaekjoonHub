a, b = map(int, input().split())
b_list = list(map(int, input().split()))

for i in range (a):
    if b_list[i] < b:
        print(b_list[i], end=" ")
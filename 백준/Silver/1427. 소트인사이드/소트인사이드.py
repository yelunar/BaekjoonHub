a = list(map(int, input()))
a.sort(reverse=True)

ans = ''
for i in range(len(a)):
    ans += str(a[i])
print(ans)
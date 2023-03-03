a = list(map(int, input()))
a.sort(reverse=True)

ans = ''
for i in range(len(a)):
    ans += str(a[i])
print(ans)

# 풀이2-------------------------
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

a = list(input().rstrip())
a.sort(reverse=True)

ans = ''
for i in range(len(a)):
    ans += str(a[i])
print(ans)

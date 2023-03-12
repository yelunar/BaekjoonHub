arr = []
n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    arr.insert(l[i],i+1)
print(*arr[::-1])
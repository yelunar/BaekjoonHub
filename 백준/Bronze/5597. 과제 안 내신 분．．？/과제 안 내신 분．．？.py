n = [i for i in range (1,31)]

for _ in range (28):
    a = int(input())
    n.remove(a)

print(min(n))
print(max(n))
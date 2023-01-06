num = set(range(1, 10001))
new = set()

for i in range (1, 10001):
    for j in str(i):
        i += int(j)
    new.add(i)
num = num - new
for i in sorted(num):
    print(i)
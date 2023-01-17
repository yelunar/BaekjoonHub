import sys
import math

t = int(input())
site = 1

for i in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(1)
    else:
        for i in range(t):
            site = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
        print(site)
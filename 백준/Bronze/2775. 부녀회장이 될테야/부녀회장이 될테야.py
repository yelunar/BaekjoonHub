t = int(input()) # test case


for i in range(t):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]

    for j in range(k):
        for k in range(1, n):
            people[k] += people[k-1]

    print(people[-1]) # 제일 꼭대기 사람수 리턴
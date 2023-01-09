num = int(input())
hansu = 0

for i in range (1, num+1):
    if i <= 99: #1~99까지는 모두 한수임
        hansu += 1
    else:
        nums = list(map(int,str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1
print(hansu)
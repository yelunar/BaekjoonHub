# 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
word = input()
croatia = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']

for i in croatia:
    word = word.replace(i, '0')

print(len(word))
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
 증가하는 순서로 배열
"""
def DFS(idx, cnt):
    if cnt == L:
        a, v = 0, 0 # a-> 자음개수 / v-> 모음개수 카운트
        for i in range(L):
            if ans[i] in vowel:
                v +=1
            else:
                a += 1
        if v>=1 and a>=2:
            print("".join(ans))
        return

    for i in range(idx, C):
        ans.append(words[i])
        DFS(i+1, cnt+1)
        ans.pop()
     

L, C = map(int, input().split()) # 서로 다른 L개의 알파벳 소문자, 사용문자 종류 C
words = sorted(list(input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']
ans = []
DFS(0, 0)
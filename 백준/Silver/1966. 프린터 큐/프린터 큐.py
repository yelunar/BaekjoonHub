from collections import deque

T = int(input())
for tc in range(T):
    n, m = map(int, input().split()) # 문서개수 / 궁금한문서가 몇번짼지
    q = deque(list(map(int, input().split()))) # 중요도
    idx = deque(list(range(n))) # 문서 인덱스 저장
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            pop_idx = idx.popleft()
            if pop_idx == m:
                print(cnt)
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
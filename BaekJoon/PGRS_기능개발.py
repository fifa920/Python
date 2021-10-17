from collections import deque

def find(q):
    cnt = 0

    while len(q) !=0 and q[0] >= 100:
        q.popleft()
        cnt += 1
    return cnt

def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    q_s = deque(speeds)

    while len(q) != 0:
        q = [x+y for x,y in zip(q,q_s)]
        q = deque(q)
        if q[0] >= 100:
            answer.append(find(q))


    return answer

solution(progresses, speeds)
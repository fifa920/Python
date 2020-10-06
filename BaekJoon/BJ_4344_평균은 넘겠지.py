import sys
sys.stdin = open("BJ_4344_평균은 넘겠지.txt", "r")

T = int(input())

for t in range(T):
    scores_list = list(map(int, input().split()))
    scores = 0
    cnt = 0

    for i in range(1,len(scores_list)):
        scores +=  scores_list[i]
    avg = scores / scores_list[0]

    for j in range(1,len(scores_list)):
        if scores_list[j] > avg :
            cnt += 1
    result = cnt/scores_list[0] * 100
    print("%0.3f%%" %result)
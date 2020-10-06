import sys
sys.stdin = open("BJ_1546_평균.txt", "r")

N = int(input())
scores_list = list(map(int, input().split()))
new_scores_list = []

M = max(scores_list)
for score in scores_list:
    new_scores_list.append(score/M*100)

avg = sum(new_scores_list)/N
print(avg)
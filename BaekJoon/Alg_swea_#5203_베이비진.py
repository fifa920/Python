import sys
sys.stdin = open('Alg_swea_#5203_베이비진.txt', 'r')

# run 혹은 triplet 인지 확인하는 함수 check(arr)
def check(arr):


T = int(input())

for tc in range(1,T+1):
    cards = list(map(int, input().split()))
    N = len(cards)
    # print(cards)
    p1 = [0] * 10
    p2 = [0] * 10
    for n in range(N):
        if n % 2 == 0 :
            p1[cards[n]] += 1
            check(p1)
        else :
            p2[cards[n]] += 1
            check(p2)


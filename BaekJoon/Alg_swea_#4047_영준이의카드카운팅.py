import sys
sys.stdin = open("Alg_swea_#4047_영준이의카드카운팅.txt", "r")

T = int(input())
dict ={'S' : 0, 'D': 1, 'H': 2, 'C': 3}

for t in range(1,T+1):
    S = input()
    cnt = [13] * 4 # S D H C 순서로 13개씩 카드가 존재
    N = len(S)
    cards = set()

    for i in range(0,N,3):
        temp = S[i:i+3]
        if temp in cards:
            print("#{} ERROR".format(t))
            break
        cards.add(temp)
        cnt[dict[temp[0]]] -= 1
    else:
        print("#{}".format(t), end=' ')
        print(*cnt)
import sys
sys.stdin = open("baekjoon_#2798_블랙잭.txt", "r")

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
hap_list = []

for i in range(0,N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            x = card_list[i] + card_list[j] + card_list[k]
            if x <= M :
                hap_list.append(x)

print(max(hap_list))

#print(card_list)
import sys
sys.stdin = open("Alg_swea_#1215_회문1.txt", "r")

T = 10

for t in range(1,T+1) :
    N = int(input())
    pan = [list(input()) for _ in range(8)]
    count = 0

    for i in range(8) :
        for j in range(9-N) :
            check = 0

            for z in range(N//2) :
                if pan[i][j+z] == pan[i][j+N-z-1] :
                    check += 1

            if check == N//2 :
                count += 1

    for i in range(8):
        for j in range(9-N):
            check = 0

            for z in range(N // 2):
                if pan[j+z][i] == pan[j+N-z-1][i]:
                    check += 1

            if check == N // 2:
                count += 1

    print(f'#{t} {count}')
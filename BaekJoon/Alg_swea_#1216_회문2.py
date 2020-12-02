import sys
sys.stdin = open("Alg_swea_#1216_회문2.txt", "r")

T = 10

for t in range(1,T+1) :
    x = int(input())
    pan = [list(input()) for _ in range(100)]
    N = 2

    for i in range(100) :
        for j in range(101- N) :
            check_a = 0

            for z in range(N // 2):                             # 회문인지 검사하기 위해 자리비교
                if pan[i][j + z] == pan[i][j - z - 1]:
                    check_a += 1
                else :
                    break
            if check_a == N//2 :                # 길이가 N 짜리 회문이면,
                N += 1



    print(N)






    '''
    count = 0
    N = 1
    M = 1



    for i in range(100):
        for j in range(101 - N):
            check_a = 0

            for z in range(N // 2):     # 회문인지 검사하기 위해 자리비교
                if pan[i][j + z] == pan[i][j + N - z - 1]:
                    check_a += 1
                else:
                    break
            if check_a == N // 2:       # 회문이면
                N += 1
                break
            else :
                continue


    for i in range(100):
        for j in range(101 - M):
            check_b = 0

            for z in range(M // 2):
                if pan[j + z][i] == pan[j + M - z - 1][i]:
                    check_b += 1
                else :
                    break
            if check_b == M // 2:
                M += 1
                break
                
    print(max(N,M))'''
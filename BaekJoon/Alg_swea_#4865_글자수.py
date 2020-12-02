import sys
sys.stdin = open ("Alg_swea_#4865_글자수.txt", "r")

T = int(input())

for t in range(1,T+1) :
    str1 = input()
    str2 = input()
    str1_list = [0] * len(str1)
    str2_list = [0] * len(str2)

    for i in range(len(str1)) :
        for j in range(len(str2)) :
            if str1[i] == str2[j] :
                str1_list[i] += 1

    print(f'#{t} {max(str1_list)}')
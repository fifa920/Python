import sys
sys.stdin = open("Alg_swea_#4047_카드카운팅.txt", "r")

T = int(input())

for t in range(1,T+1) :
    input_card = list(input())
    lst = [[1 for _ in range(13)] for _ in range(4)]
    count_list=[]
    cnt = 0



    for n in range(0,len(input_card),3) :
        if input_card[n] == 'S' :
            lst[0][int(input_card[n+1]+input_card[n+2])-1] -= 1
        elif input_card[n] == 'D' :
            lst[1][int(input_card[n + 1] + input_card[n + 2])-1] -= 1
        elif input_card[n] == 'H':
            lst[2][int(input_card[n + 1] + input_card[n + 2])-1] -= 1
        elif input_card[n] == 'C':
            lst[3][int(input_card[n + 1] + input_card[n + 2])-1] -= 1

    for i in range(4) :
        for j in range(13) :
            if lst[i][j] < 0 :
                cnt += 1
                break

    if cnt == 0 :
        for i in range(4) :
            count_list.append(sum(lst[i]))
        print(f'#{t}', end=' ')
        print(*count_list)
    else :
        print(f'#{t} ERROR')



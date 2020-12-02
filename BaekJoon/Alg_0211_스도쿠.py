import sys
sys.stdin = open("스도쿠.txt","r")
T = int(input())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]     #12시부터 시계방향으로
dy = [0, 1, 1, 1, 0, -1, -1, -1]


for t in range(1,T+1) :
    lst = [list(map(int, input().split())) for _ in range(9)]  #(1,1) (1,4) (1,7) (4,1) (4,4) (4,7) (7,1), (7,4) (7,7) 을 검증

    isTrue = True
    temp = True

    # (1,1) 에서 먼저 하자
    for p in (1,4,7) :
        for q in (1,4,7) :
            num_list = []
            num_list.append(lst[p][q])
            for i in range(8):
                newX, newY = 0, 0
                newX = p + dx[i]
                newY = q + dy[i]
                if lst[newX][newY] not in num_list:
                    num_list.append(lst[newX][newY])

            if len(num_list) != 9 : # 모두 탐색할 필요 없이 9개의 숫자 안되면 temp 를 False로 주고 빠져나옴
                temp = False
                break
        if temp == False :
            isTrue = False
            break


    #print(isTrue)


    if isTrue == True :
        for i in range(9) :
            if sum(lst[i][:]) != 45 or sum(lst[:][i]) != 45 :
                isTrue = False
                break
            else :
                print(isTrue)



    print(isTrue)



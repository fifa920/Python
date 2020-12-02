import sys
sys.stdin = open("Alg_03_cardplay.txt", "r")

T = int(input())

for t in range(T) :
    information = input()
    card_lst = [13] * 4
    card_check = []
    isError = True


    for i in range(0,12,3) :            # [S01, D02 ...] 이렇게 만듬
        card_check += [information[i] + information[i+1] + information[i+2]]

    #print(card_check)

    for x in card_check :
        if card_check.count(x) > 1 :
            isError = False
            break


        else :
            if x[0] == 'S':
                card_lst[0] -= 1

            elif x[0] == 'D':
                card_lst[1] -= 1

            elif x[0] == 'H':
                card_lst[2] -= 1

            elif x[0] == 'C':
                card_lst[3] -= 1

    if isError == False :
        print('\nERROR')
    else :
        for x in card_lst :
            print(x, end=' ')




import sys
sys.stdin = open("List1_card_hw3.txt", "r")

T = int(input())

if 1<= T <= 50 :

    for i in range(1,T+1) :
        N = int(input())
        cards = input() # 문자 형태로 들어오지만 index로 접근 가능하다. 대신 int(cards[i]) 변환해서 쓰기.
        #print(cards)
        if 5 <= N <= 100 :

            cnt = [0]*10 # 0~9 까지 자리 만들어서 count 함
            for j in range(0,N) :
                cnt[int(cards[j]) % 10] += 1

            maxcnt = 0
            maxidx = 0
            for k in range(len(cnt)) :
                if cnt[k] >= maxcnt:
                    maxcnt = cnt[k]
                    maxidx = k


        print('#{0} {1} {2}'.format(i, maxidx, maxcnt))








else :
    print('T가 허용 범위를 벗어났습니다.')
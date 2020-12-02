import sys
sys.stdin = open("1206input.txt","r")

tc = 10

for i in range(tc) :

        N = int(input())
        Hs = list(map(int, input().split()))
        vSum = 0

        for j in range(2, N-2) :
            maxH = 0
            # list_around = list(map(int, [-2, -1, 1, 2]))
            for k in ([-2, -1, 1, 2]):
                if maxH < Hs[j+k] :
                    maxH = Hs[j+k]
            diff = Hs[j] - maxH
            if diff >0 :
                vSum += diff
        print('#{0} : {1}'.format(i+1,vSum))


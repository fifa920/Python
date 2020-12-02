import sys
sys.stdin = open("series_one.txt","r")

T = int(input())

for t in range(T) :
    N = int(input())
    num_list = input()  # 010000111 을 string 으로 받음
    count = 0
    max_count = 0

    for i in range(N) :
        if num_list[i] == '0' :
            count = 0
        else :
            count += 1
        if count > max_count :
            max_count = count

    print('#{} {}'.format(t+1, max_count))






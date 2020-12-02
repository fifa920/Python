import sys
sys.stdin = open("Alg_swea_#4864_문자열비교.txt", "r")

T = int(input())
for t in range(1,T+1) :
    my_string = input()
    your_string = input()
    cnt = 0

    for x in range(len(your_string)-len(my_string)+1) :
        count = 0
        for y in range(len(my_string)):
            if my_string[y] == your_string[x+y] :
                count += 1
                continue
            else :
                break

        if count == len(my_string) :
            cnt += 1

    print(f'#{t} {cnt}')








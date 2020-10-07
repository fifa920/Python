import sys
sys.stdin = open("BJ_1009_분산처리.txt", "r")

T = int(input())
for t in range(T):
    a,b = map(int, input().split())
    a %= 10
    if a == 1 or a == 5 or a == 6 :
        print(a)
    elif a == 0 :
        print(10)
    elif a == 4 or a == 9 :
        if b % 2 :
            print(a)
        else :
            print(a*a % 10)
    else :
        b = b % 4
        if b == 0 :
            print(a**4%10)
        else :
            print(a**b%10)

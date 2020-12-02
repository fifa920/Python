import sys
sys.stdin = open("baekjoon_#1436_666.txt", "r")

N = int(input())
i = 1
valid = '666'
count = 0

while True :
    i += 1
    if valid in str(i) :
        count += 1

    if N == count :
        print(i)
        break



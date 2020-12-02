import sys
sys.stdin = open("cardplay.txt", "r")

T= int(input())

for t in range(T) :
    information = input() # 3글자씩 끊어서 받을 수 없을까?
    lst = [[1 for _ in range(13)] for _ in range(4)]
    card_list = []

    for i in information :
        card_list.append(i)


T = int(input())
for tc in range(T):
    N = int(input())
    numbers_list = list(map(int, input().split()))
    Min = numbers_list[0]
    Max = numbers_list[0]

    for i in range(1,N):
        if numbers_list[i] < Min :
            Min = numbers_list[i]
        if numbers_list[i] > Max :
            Max =  numbers_list[i]

    print("#{} {}".format(tc+1, Max-Min))

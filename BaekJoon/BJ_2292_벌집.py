N = int(input())

room = 1
result = 1
cnt_six = 6
if N == 1 :
    print(1)
else :
    while(result < N) :
        result += cnt_six
        cnt_six += 6
        room += 1

print(room)
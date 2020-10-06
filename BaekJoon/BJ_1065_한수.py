def solution(N):
    if N <= 99 :
        result = N
    elif N < 1000:
        count = 0
        for x in range(101,N+1):
            num_list = list(map(int, str(x)))
            print(num_list)
            if num_list[0] - num_list[1] == num_list[1] - num_list[2] :
                count += 1
        result = 99 + count

    else :
        result = 144
    return result

N = 310
print(solution(N))
N,M = map(int, input().split())

numbers = [i for i in range(1,N+1)]

def track(depth, ans):
    if depth == M:
        print(*ans)
    for number in numbers:
        if len(ans) == 0:
            ans.append(number)
            track(depth+1, ans)
            ans.pop()
        else:
            if number > ans[-1]:
                ans.append(number)
                track(depth+1, ans)
                ans.pop()
track(0,[])
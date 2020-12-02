import sys
sys.stdin = open ("baekjoon_#15652_N과M(4).txt", "r")

N, M = map(int, input().split())
numbers = list(range(1,N+1))

def track(depth, ans) :
    if depth == M :
        result = list(map(str, ans))
        print(' '.join(result))
        return

    for number in numbers :
        if len(ans) == 0 :
            ans.append(number)
            track(depth+1, ans)
            ans.pop()

        else :
            if number >= ans[-1] :
                ans.append(number)
                track(depth + 1, ans)
                ans.pop()

track(0, [])
import sys
sys.stdin = open("baekjoon_#14889_스타트링크.txt", "r")

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
numbers = list(range(N))
abs_list = []
x = []


def teamDiv(depth, ans):
    if depth == N / 2:
        result = list(map(int, ans))
        oppo_result = []
        for i in range(N) :
            if i not in result :
                oppo_result.append(i)
        sum_result = 0
        sum_oppo_result = 0

        for i in range(N//2) :
            for j in range(i+1,N//2) :
                sum_result += (S[result[i]][result[j]] + S[result[j]][result[i]])
                sum_oppo_result += (S[oppo_result[i]][oppo_result[j]] +S[oppo_result[j]][oppo_result[i]])
        abs_list.append(abs(sum_result - sum_oppo_result))

        return

    for number in numbers:
        if len(ans) == 0:
            ans.append(number)
            teamDiv(depth + 1, ans)
            ans.pop()

        else:
            if number > ans[-1]:
                ans.append(number)
                teamDiv(depth + 1, ans)
                ans.pop()



teamDiv(0,[])
print(min(abs_list))
N = int(input())
min_list = list(map(int, input().split()))
result_list = sorted(min_list)
result = 0

for i in range(len(min_list)):
    result += result_list[i]*(N-i)
print(result)
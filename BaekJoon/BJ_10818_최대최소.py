N = int(input())
num_list = list(map(int, input().split()))
# num_list = [10,20,1,6,14,19,64,12,3,4,5]
max_num = num_list[0]
min_num = num_list[0]

for num in num_list:
    if num > max_num :
        max_num = num
    if num < min_num :
        min_num = num

print(min_num, max_num)
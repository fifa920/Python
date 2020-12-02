import sys
sys.stdin = open("baekjoon_#2309_일곱난쟁이.txt","r")

height_list = []
for _ in range(9):
    height_list.append(int(input()))

standard = 100
total = sum(height_list)
result = total-standard
N = len(height_list)
result_list=[]

for idx1 in range(N-1):
    flag = False
    for idx2 in range(idx1+1,N):
        if height_list[idx1] + height_list[idx2] == result :
            height_list[idx1] = height_list[idx2] = 0
            flag = True
            break
    if flag:
        break

for x in height_list:
    if x != 0 :
        result_list.append(x)
result_list.sort()

for i in result_list:
    print(i, sep='\n')

# print(height_list)

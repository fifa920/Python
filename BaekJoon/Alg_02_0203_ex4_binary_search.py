import sys

sys.stdin = open("Alg_02_0203_ex4_binary_search.txt","r")

srted_data = list(map(int, input().split()))
n = len(srted_data)
start = 0
end = n-1
print('찾으려는 수를 입력하시오 : ')
x = int(input())
IsFound = False

while start <= end :
    middle = (start + end) // 2

    if x > srted_data[middle] :
        start = middle + 1

    elif x < srted_data[middle] :
        end = middle -1

    else :
        IsFound = True
        print('{0} 는 존재합니다.'.format(x))
        break
if IsFound == 0 :
    print('{0} 는 존재하지 않습니다.'.format(x))



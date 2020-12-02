
arr = [4, 9, 11, 23, 2, 19, 7]
x = int(input('찾고자 하는 수를 입력하시오 : '))
IsFound = False

for i in range(len(arr)) :
    if x == arr[i] :
        IsFound = True
        print('{0}는 존재합니다.'.format(x))
        break

if IsFound == False :
    print('못 찾았습니다.')


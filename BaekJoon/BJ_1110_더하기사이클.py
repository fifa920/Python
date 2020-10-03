# num = int(input())
num = 0
check = num
count = 1
new_num = 0

while True :
    temp = num // 10 + num % 10
    if temp >= 10:
        temp = temp % 10
    else :
        pass
    num = num%10*10 + temp
    if check == num :
        break
    count += 1

print(count)
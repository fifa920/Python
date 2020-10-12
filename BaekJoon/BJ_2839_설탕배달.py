kg = int(input())

Max_m = kg//5

if kg % 5 == 0 :
    print(Max_m)
else :
    flag = 0
    for i in range(Max_m,-1,-1):
        if (kg-5*i) % 3 == 0 :
            result = i+(kg-5*i)//3
            flag = 1
            print(result)
            break
    if flag == 0 :
        print(-1)

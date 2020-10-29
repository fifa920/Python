N = int(input())
change = 1000 - N

changes_list = [500, 100, 50, 10, 5, 1]
result = 0

for i in changes_list:
    if change // i != 0 :
        result += change // i
        change = change % i
print(result)
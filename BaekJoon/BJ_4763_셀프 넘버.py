def SelfNum(number):
    part = 0
    for num in str(number):
        part += int(num)
    result = number + part
    return result

numbers = list(range(1,10001))
generated_numbers = []

for num in numbers:
    gen = SelfNum(num)
    if gen < 10000:
        generated_numbers.append(gen)

num_list = list(range(1,10000))

for num in num_list:
    if num in generated_numbers:
        pass
    else :
        print(num)
# pan = list(map(int, input().split()) for _ in range(9))

numbers = [i for i in range(1,10)]

def check_row():
    for y in range(1,10):
        for x in range(1,10):
            
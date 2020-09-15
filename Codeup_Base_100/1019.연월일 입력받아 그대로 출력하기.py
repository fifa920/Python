# zfill 을 사용하여 자리수를 정하고 나머지를 빈칸으로 채울 수 있다.

year, month, day = input().split('.')
print(year.zfill(4), month.zfill(2), day.zfill(2), sep='.')

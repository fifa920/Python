year, month, date = input().split('.')

print('{}-{}-{}'.format(date.zfill(2), month.zfill(2), year.zfill(4)))
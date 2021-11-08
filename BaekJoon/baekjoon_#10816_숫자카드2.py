N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
cards.sort()
# print(cards)
number_dict = {x : 0 for x in targets}
# print(number_dict)

for target in targets:
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if target == cards[mid]:
            number_dict[target] = cards.count(target)
            break
        elif target < cards[mid]:
            end = mid-1
        else:
            start = mid+1
    if target in cards:
        print(number_dict[target], end=' ')
    else:
        print(0, end=' ')

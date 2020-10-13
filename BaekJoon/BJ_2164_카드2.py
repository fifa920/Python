from collections import deque

N = int(input())
cards_list = deque(list(range(1,N+1)))
# print(cards_list)

while len(cards_list) != 1 :
    cards_list.popleft()
    x = cards_list.popleft()
    cards_list.append(x)

print(*cards_list)
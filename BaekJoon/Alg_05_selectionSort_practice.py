#선택정렬을 재귀를 이용해서 만들기 !!!!!!!!!!!

Data = [3, 2, 5, 1, 6, 10]

def Getsome(here, end) :
    
    if here >= end : return

    #3. basecase를 3번 작성

    minmin = Data[here]

    #1. 무엇이 반복되고 있는지

    where = here
    for now in range(here, end + 1) :
        if Data[now] < minmin :
            minmin = Data[now]
            where= now
    Data[here], Data[where] = Data[where], Data[here]

    #2. 크기를 바꿔서 재귀로 호출

    Getsome(here+1, end)

Getsome(0, 4)
print(Data)
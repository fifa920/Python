def binarysearch(S,x):
    low = 0
    high = len(S)
    location = 0
    while (low <= high and location == 0) :
        mid = (low+high)//2
        if S[mid] == x :
            location = mid
        elif x > S[mid] :
            low = mid + 1
        else :
            high = mid - 1

    return location

S = [1, 3, 10, 20, 33, 34, 39, 41, 49]

print(binarysearch(S,3))

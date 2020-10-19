def location(S,low,high):
    if low > high :
        return 0
    else :
        mid = (low+high)//2
        if x == S[mid] :
            return mid
        elif S[mid] > x:
            return location(S,low,mid-1)
        else :
            return location(S,mid+1,high)

arr = [1,2,5,7,10,17,25,35,37,38,39,68,77,90]
x = 10
print(location(arr,0,len(arr)))
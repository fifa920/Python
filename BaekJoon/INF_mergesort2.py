def mergesort2(S,low, high):
    if high < low :
        mid = (low+high) // 2
        mergesort2(S,low,mid)
        mergesort2(S,mid+1,high)
        merge2 (S,low,mid,high)

def merge2(S,low,mid,high):
    U = []
    i = low
    j = mid + 1
    while i <= mid and j <= high :
        if S[i] < S[j] :
            S.append(S[i])
            i += 1
        else :
            S.append(S[j])
            j += 1
        if i <= mid :
            U += S[i : mid+1]
        else :
            S += S[j : high+1]

        for k in range(low,high+1):
            S[k] = U[ k - low ]
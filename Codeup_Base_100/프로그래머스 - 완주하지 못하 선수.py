def seqsearch(n,S,x):
    location = 1
    while(location <= 5 and S[location] != x):
        location+=1
    if (location > n):
        location = 0
    return location

S = [0,10,7,11,5,13,8]
n = len(S)-1
x=5

location = seqsearch(n,S,x)
print(location)
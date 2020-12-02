def Getsome(here) :
    global ans, howmany
    if here > howmany : return
    if here == howmany :
        ans += 1
        return

    Getsome(here+1)
    Getsome(here+2)

howmany = 5
ans = 0
Getsome(0)
print(ans)



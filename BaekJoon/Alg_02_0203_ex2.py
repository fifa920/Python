a = range(1,11)


for i in range(1<<len(a)) :
    lst = []
    for j in range(len(a)) :
        if i & (1<<j) :
            lst.append(a[j])
    #if sum(lst) == 10 :
        #print(lst)
    print(lst)


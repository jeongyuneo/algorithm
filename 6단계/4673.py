def selfNum():
    a = list(i for i in range(10001))
    #print(a)
    for i in range(1, 10000):
        if i < 10:
            idx = i + i
        elif i < 100:
            idx = i + int(i/10) + int(i%10)
        elif i < 1000:
            idx = i + int(i/100) + int((i%100)/10) + int(i%10)
        else:
            idx = i + int(i/1000) + int((i%1000)/100) + int((i%100)/10) + int(i%10)

        if idx in a:
            a[idx] = 0
    for i in a:
        if i != 0:
            print(i)

selfNum()
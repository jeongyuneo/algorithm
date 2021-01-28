croAlpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
tmpStr = ''
cnt = 0
i = 0
while i < len(a):
    tmpStr += a[i]
    if len(tmpStr) > 2:
        if tmpStr in croAlpha:
            tmpStr = ''
            cnt += 1
            i += 1
            continue
        elif tmpStr[:2] in croAlpha:
            tmpStr = ''
            cnt += 1
            continue
        else:
            tmpStr = tmpStr[1:]
            cnt += 1
            if tmpStr in croAlpha:
                tmpStr = ''
                cnt += 1
                i += 1
                continue
    if not tmpStr in croAlpha and i == len(a) - 1:
        cnt += len(tmpStr)
    if tmpStr in croAlpha and i == len(a) - 1:
        cnt += 1
    i += 1
print(cnt)

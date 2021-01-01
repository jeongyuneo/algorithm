a = int(input())
b = input()
s1 = a * int(b[2])
s2 = a * int(b[1])
s3 = a * int(b[0])
s4 = s3 * 100 + s2 * 10 + s1
print('%d\n%d\n%d\n%d'%(s1, s2, s3, s4))
a, b = map(int, input().split())
if a > 0 and b < 45:
    a -= 1
    b += 15 # b = b - 45 + 60
elif a < 1 and b < 45:
    a = 23
    b += 15 # b = b - 45 + 60
else:
    b -= 45
print(a, b)
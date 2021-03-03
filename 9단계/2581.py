m = int(input())
n = int(input())
min_value = 0
sum_values = 0
prime_numbers = []
for i in range(m, n+1):
    if i == 1:
        continue
    j = 2
    while j <= i:
        if j == i:
            prime_numbers.append(i)
        if i % j == 0:
            break
        j += 1

if len(prime_numbers) == 0:
    print(-1)
else:
    print(sum(prime_numbers))
    print(min(prime_numbers))
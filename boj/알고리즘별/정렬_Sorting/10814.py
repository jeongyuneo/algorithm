import sys

n = int(input())
members = []
for i in range(n):
    age, name = sys.stdin.readline().rsplit()
    members.append([int(age), name])
members.sort(key=lambda x: x[0])
for a, n in members:
    print(a, n)
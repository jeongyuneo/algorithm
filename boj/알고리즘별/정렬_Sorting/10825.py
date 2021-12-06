n = int(input())
members = []
for i in range(n):
    name, kor, eng, math = map(str, input().split())
    members.append([name, int(kor), int(eng), int(math)])
members.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for member in members:
    print(member[0])
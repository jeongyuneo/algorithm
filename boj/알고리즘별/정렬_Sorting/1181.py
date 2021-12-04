import sys

n = int(input())
words = list(set(sys.stdin.readline().rstrip() for _ in range(n)))
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)
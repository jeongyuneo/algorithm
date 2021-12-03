import sys

shortcuts = []
results = []

n = int(input())
for i in range(n):
    words = list(sys.stdin.readline().strip().split(' '))
    result_list = []
    for j in range(len(words)):
        if words[j][0].lower() not in shortcuts:
            shortcuts.append(words[j][0].lower())
            words[j] = words[j].replace(words[j][0], '[' + words[j][0] + ']', 1)
            break
    result_string = ' '.join(words)
    if '[' not in result_string:
        for j in range(1, len(result_string)):
            if result_string[j] != ' ' and result_string[j].lower() not in shortcuts:
                shortcuts.append(result_string[j].lower())
                result_string = result_string.replace(result_string[j], '['+result_string[j]+']', 1)
                break
    results.append(result_string)
for result in results:
    print(result)
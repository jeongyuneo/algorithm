import re

alphabets = re.compile('[a-z]+')

n = int(input())
result = []
for i in range(n):
    input_value = input()
    result.extend(alphabets.split(input_value))
answers = []
for value in result:
    if value != '':
        answers.append(int(value))
for answer in sorted(answers):
    print(answer)
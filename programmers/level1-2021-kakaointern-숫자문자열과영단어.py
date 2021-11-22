numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def solution(s):
    if s.isnumeric():
        return int(s)
    answer = 0
    english_number = ""
    for idx in s:
        if idx.isnumeric():
            answer *= 10
            answer += int(idx)
        else:
            english_number += idx
        if english_number in numbers:
            answer *= 10
            answer += numbers[english_number]
            english_number = ""
    return answer

a = [
    "one4seveneight",
    "23four5six7",
    "2three45sixseven",
    "123"
]

for x in a:
    print(solution(x))
def solution(s):
    compressed_strings = []
    n = len(s)
    for i in range(int(n/2)+1):
        sliced_string = []
        for j in range(0, n, i+1):
            if j + i + 1 >= n:
                idx = n
            else:
                idx = j + i + 1
            sliced_string.append(s[j:idx])
        m = len(sliced_string)
        k = 0
        cnt = 1
        compressing_string = ''
        while k < m:
            while k < m - 1 and sliced_string[k] == sliced_string[k + 1]:
                cnt += 1
                k += 1
            if cnt == 1:
                compressing_string += sliced_string[k]
            else:
                compressing_string += str(cnt) + sliced_string[k]
            k += 1
            cnt = 1
        compressed_strings.append(compressing_string)
    answer = len(sorted(compressed_strings, key=len)[0])
    return answer

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]

for x in a:
    print(solution(x))
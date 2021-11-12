import re

allowed_strings = re.compile('[a-z|0-9|\-|_|.]')
repeated_dot = re.compile('[.]+')
beginnings = re.compile('^[.].*')
endings = re.compile('.*[.]$')

def solution(new_id):
    new_id_round_1 = new_id.lower()
    new_id_round_2 = ''
    for idx in allowed_strings.findall(new_id_round_1):
        new_id_round_2 += idx
    new_id_round_3 = repeated_dot.sub('.', new_id_round_2)
    new_id_round_4 = new_id_round_3
    if beginnings.match(new_id_round_3):
        new_id_round_4 = new_id_round_4[1:]
    if endings.match(new_id_round_3):
        new_id_round_4 = new_id_round_4[:-1]
    new_id_round_5 = new_id_round_4
    if new_id_round_5 == '':
        new_id_round_5 = 'a'
    new_id_round_6 = new_id_round_5
    if len(new_id_round_6) >= 16:
        new_id_round_6 = new_id_round_6[:15]
        if endings.match(new_id_round_6):
            new_id_round_6 = new_id_round_6[:-1]
    new_id_round_7 = new_id_round_6
    if len(new_id_round_7) <= 2:
        while len(new_id_round_7) != 3:
            new_id_round_7 += new_id_round_7[len(new_id_round_7)-1]
    answer = new_id_round_7
    return answer

a = [
    "...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p"
]
for x in a:
    print(solution(x))
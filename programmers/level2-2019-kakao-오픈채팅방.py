from collections import defaultdict

def solution(record):
    answer = []
    user_dict = defaultdict(str)
    for idx in record:
        if idx.startswith('Enter') or idx.startswith('Change'):
            act, user_id, user_nickname = idx.split(" ")
        user_dict[user_id] = user_nickname
    for idx in record:
        if idx.startswith('Enter'):
            answer.append("%s님이 들어왔습니다." % user_dict.get(idx.split()[1]))
        elif idx.startswith('Leave'):
            answer.append("%s님이 나갔습니다." % user_dict.get(idx.split()[1]))
    return answer

a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(a))
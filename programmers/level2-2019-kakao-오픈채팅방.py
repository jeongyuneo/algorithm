from collections import defaultdict

def solution(record):
    answer = []
    user_dict = defaultdict(str)
    split_record = []
    for i in record:
        if 'Change' in i or 'Enter' in i:
            act, user_id, user_nickname = i.split(" ")
            split_record.append([act, user_id, user_nickname])
        else:
            act, user_id = i.split(" ")
            split_record.append([act, user_id])
            continue
        user_dict[user_id] = user_nickname
    for i in split_record:
        if 'Enter' in i:
            answer.append("%s님이 들어왔습니다." % user_dict.get(i[1]))
        elif 'Leave' in i:
            answer.append("%s님이 나갔습니다." % user_dict.get(i[1]))
    return answer

a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(a))
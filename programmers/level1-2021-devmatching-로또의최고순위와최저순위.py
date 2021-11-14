def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for idx in lottos:
        if idx in win_nums:
            cnt += 1
    best_cnt, worst_cnt = cnt+lottos.count(0), cnt
    best_ranking, worst_ranking = get_ranking(best_cnt), get_ranking(worst_cnt)
    answer.append(best_ranking)
    answer.append(worst_ranking)
    return answer

def get_ranking(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6

a = [
    [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]],
    [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]],
    [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]]
]

for x in a:
    print(solution(x[0], x[1]))
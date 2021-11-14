def solution(lottos, win_nums):
    answer = []
    cnt = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    for idx in lottos:
        if idx in win_nums:
            cnt += 1
    best_ranking, worst_ranking = rank[cnt+lottos.count(0)], rank[cnt]
    answer.extend([best_ranking, worst_ranking])
    return answer

a = [
    [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]],
    [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]],
    [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]]
]

for x in a:
    print(solution(x[0], x[1]))
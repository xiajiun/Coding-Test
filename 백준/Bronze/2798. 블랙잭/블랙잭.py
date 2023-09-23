N, M = map(int, input().split())
card = list(map(int, input().split()))

from itertools import combinations
combi_sum_list = []
for combi in combinations(card, 3):
    if sum(combi) <= M:
        combi_sum = sum(combi)
        combi_sum_list.append(combi_sum)
print(max(combi_sum_list))
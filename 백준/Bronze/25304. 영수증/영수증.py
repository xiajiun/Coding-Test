total = int(input())
sum_list = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    sum_one = a*b
    sum_list.append(sum_one)
total_count = sum(sum_list)
if total_count == total:
    print('Yes')
else: 
    print('No')
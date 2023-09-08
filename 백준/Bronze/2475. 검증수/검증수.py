li = list(map(int, input().split()))
total_list = []
for i in li:
    total_list.append(i*i)
total = sum(total_list)
print(total%10)
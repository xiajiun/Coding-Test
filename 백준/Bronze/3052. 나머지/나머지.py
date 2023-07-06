count_list = []
for _ in range(10):
    i = int(input())
    remainder = i%42
    count_list.append(remainder)
remove_duplicates = set(count_list)
print(len(remove_duplicates))
num = map(int, input().split())
num_list = []
for i in num:
    rev = int(str(i)[::-1])
    num_list.append(rev)
print(max(num_list))
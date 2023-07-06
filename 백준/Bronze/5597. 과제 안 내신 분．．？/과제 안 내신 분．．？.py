submit = []
for _ in range(28):
    submit.append(int(input()))

all_list = []
for i in range(1, 31):
    all_list.append(i)

for i in all_list:
    if i in submit:
        pass
    else:
        print(i)
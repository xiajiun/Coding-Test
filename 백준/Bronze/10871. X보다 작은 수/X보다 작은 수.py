size, num =  map(int, input().split())
num_list = list(map(int, input().split()))
for i in num_list:
    if i < num:
        print(i, end=' ')
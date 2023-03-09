arr = [list(map(int, input().split())) for _ in range(5)]

sum_all = []

for i in range(5):
    sumv=0
    for j in range(4):
        sumv += arr[i][j]
    sum_all.append(sumv)
    
max_num = max(sum_all)
index = sum_all.index(max_num)
print(index+1, max_num)

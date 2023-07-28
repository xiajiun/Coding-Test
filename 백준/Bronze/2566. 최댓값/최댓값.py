m = []

for item in range(9):
    item = list(map(int, input().split()))
    m.append(item)

max_num = 0
row = 0
column = 0
for idx_row, i in enumerate(m):
    for idx_col, j in enumerate(i):
        if j >= max_num:
            max_num = j
            row = idx_row + 1
            column = idx_col + 1
            
print(max_num)
print(row, column)
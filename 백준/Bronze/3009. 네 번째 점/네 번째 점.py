list_x = []
list_y = []
for _ in range(3):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)
for i in list_x:
    if list_x.count(i) == 1:
        vertex_x = i
for j in list_y:
    if list_y.count(j) == 1:
        vertex_y = j
print(vertex_x, vertex_y)
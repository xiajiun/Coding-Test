a, b, c = map(int, input().split())
tri_list = [a, b, c]
tri_list = sorted(tri_list)
if tri_list[2] >= tri_list[1] + tri_list[0]:
    tri_list[2] = tri_list[1] + tri_list[0] - 1
    print(sum(tri_list))
else:
    print(sum(tri_list))
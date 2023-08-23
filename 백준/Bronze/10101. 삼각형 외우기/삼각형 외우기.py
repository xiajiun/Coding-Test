angle_list = []
for _ in range(3):
    angle_list.append(int(input()))
if sum(angle_list) == 180:
    if angle_list[0] == angle_list[1] == angle_list[2]:
        print('Equilateral')
    elif angle_list[0] == angle_list[1] or angle_list[1] == angle_list[2] or angle_list[0] == angle_list[2]:
        print('Isosceles')
    elif angle_list[0] != angle_list[1] != angle_list[2]:
        print('Scalene')
else:
    print("Error")
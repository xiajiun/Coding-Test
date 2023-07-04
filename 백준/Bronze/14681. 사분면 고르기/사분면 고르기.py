num = [input() for _ in range(2)]
a = int(num[0])
b = int(num[1])

if a >= 0:
    if b >= 0:
        print('1')
    else: print('4')
else: #negative
    if b >= 0:
        print('2')
    else: print('3')
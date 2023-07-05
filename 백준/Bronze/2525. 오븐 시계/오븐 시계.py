num = [input() for _ in range(2)]
a, b = map(int, num[0].split())
c = num[1]
c = int(c)

b = b + c
a = a + (b//60)
if a >= 24:
    a = a - 24
b = b % 60

print(a, b)
a, b = map(int, input().split())

if b < 45:
    if a == 0:
        a = a + 24
    else: a = a
    a = a - 1
    b = b + 60 - 45
else:
    a = a
    b = b - 45
print(a, b)

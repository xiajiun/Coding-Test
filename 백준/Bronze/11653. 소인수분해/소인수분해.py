nr = int(input())
i = 2
factors = []
while i <= nr:
    if (nr % i) == 0:
        factors.append(i)
        nr = nr / i
    else:
        i = i + 1
for i in factors:
    print(i)
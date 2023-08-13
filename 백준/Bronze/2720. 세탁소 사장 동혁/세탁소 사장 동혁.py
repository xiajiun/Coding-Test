coin = [25, 10, 5, 1]
for _ in range(int(input())):
    change = int(input())
    for i, j in enumerate(coin):
        a = change // j
        b = change % j
        change = b
        print(a, end=' ')
    print()
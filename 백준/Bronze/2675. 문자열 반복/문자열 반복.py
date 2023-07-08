n = int(input())
for _ in range(n):
    size, word = input().split()
    size = int(size)
    word = str(word)
    for i in word:
        print(i*size, end='')
    print()
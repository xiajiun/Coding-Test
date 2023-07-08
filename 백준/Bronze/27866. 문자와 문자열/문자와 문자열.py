word = input()
index = int(input())
for idx, i in enumerate(word):
    if (idx+1) == index:
        print(i)
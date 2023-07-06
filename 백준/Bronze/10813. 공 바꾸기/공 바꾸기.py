size, ball = map(int, input().split())
bag = []
for i in range(size):
    bag.append(i+1)
for _ in range(ball):
    i, j = map(int, input().split())
    bag[i-1], bag[j-1] = bag[j-1], bag[i-1]
for item in bag:
    print(item, end=' ')
size, ball = map(int, input().split())
bag = [0]*size
for _ in range(ball):
    start, end, num = map(int, input().split())
    for i in range(start-1, end):
        bag[i] = num

for i in bag:
    print(i, end=' ')
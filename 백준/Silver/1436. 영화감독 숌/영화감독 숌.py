num = 1
n = int(input())
count = 0
while True:
    if '666' in str(num):
        count = count + 1
    if count == n:
        break
    num = num + 1
print(num)
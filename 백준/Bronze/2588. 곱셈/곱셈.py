number = [input() for _ in range(2)]
a = int(number[0])
b = int(number[1])

print(a*int(str(b)[2:]))
print(a*int(str(b)[1:2]))
print(a*int(str(b)[:1]))
print(a*b)
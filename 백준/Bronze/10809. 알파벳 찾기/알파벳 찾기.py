S = input()
abc = [chr(abc) for abc in range(ord('a'), ord('z')+1)]

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')
while True:
    p = int(input())
    if p == -1:
        break
    num_list = []
    for i in range(1, p+1):
        if p/i != p:
            if p % i == 0:
                num_list.append(int(p/i))
    num_list.sort()
    if sum(num_list) == p:
        print(p,'=',' + '.join(map(str, num_list)))
    else:
        print(p,'is NOT perfect.')
a = int(input())
b = int(input())
sosu_list = []
for num in range(a, b+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수.
if len(sosu_list) != 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else: print(-1)
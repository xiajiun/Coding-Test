size = int(input())
num_list = list(map(int, input().split()))

max_num = max(num_list)
new_list = []
for index, num in enumerate(num_list):
    avg = num_list[index]/max_num*100
    new_list.append(avg)
average = sum(new_list)/size
print(average)
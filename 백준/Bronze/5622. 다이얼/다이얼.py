alp_list = ['','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','']
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
alp_dict = dict(zip(alp_list, num_list))

total = 0
word = input()
for key, value in alp_dict.items():
    for i in word:
        if i in key:
            total += value + 1
print(total)
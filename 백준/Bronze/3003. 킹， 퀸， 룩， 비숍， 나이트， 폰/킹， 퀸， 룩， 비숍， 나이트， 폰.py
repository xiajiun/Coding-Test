ori_list = [1,1,2,2,2,8]
mod_list = list(map(int, input().split()))
for idx, i in enumerate(ori_list):
    print(i-mod_list[idx], end=' ')

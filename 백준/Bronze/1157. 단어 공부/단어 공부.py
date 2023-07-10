word = input()
word = word.upper()
list_word = []
list_idx = []
for i in word:
    if i not in list_word:
        list_word.append(i)
        list_idx.append(word.count(i))
occ = max(list_idx) 
if list_idx.count(occ) >= 2:
    print('?')
else:
    print(list_word[list_idx.index(occ)])
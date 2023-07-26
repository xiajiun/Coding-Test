dictt = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum_list = []
score_sum = []
for _ in range(20):
    subject, score, level = input().split()
    score = float(score)
    if level != 'P':
        summation = dictt[level]*score
        sum_list.append(summation)
        score_sum.append(score)

total = 0
total_score = 0
for item in sum_list:
    total = total + item
for item2 in score_sum:
    total_score = total_score + item2

print(total/total_score)
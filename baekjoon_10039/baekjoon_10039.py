# [백준 10039] 평균 점수

score_sum = 0
for i in range(0, 5):
    score = int(input())
    if score < 40:
        score = 40
    score_sum += score

print(int(score_sum/5))

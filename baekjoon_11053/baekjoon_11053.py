# [백준 11053] 가장 긴 증가하는 부분 수열

n = int(input())
sequence = list(map(int, input().split()))

dp = [1]
total_max = 1
for i in range(1, n):
    max_length = 0
    for j in range(0, i):
        if sequence[j] < sequence[i] and dp[j] > max_length:
            max_length = dp[j]
    dp.append(max_length+1)
    if dp[i] > total_max:
        total_max = dp[i]

print(total_max)

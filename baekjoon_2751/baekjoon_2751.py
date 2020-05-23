# [백준 2751] 수 정렬하기2

import sys
input = sys.stdin.readline

num_list = [0]*2000001

n = int(input())

for i in range(0, n):
    input_num = int(input())
    if input_num >= 0:
        num_list[input_num+1000000] += 1
    else:
        num_list[1000000-abs(input_num)] += 1

for i in range(0, len(num_list)):
    if num_list[i] == 1:
        print(i-1000000)



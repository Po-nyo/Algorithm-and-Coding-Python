# [백준 10989] 수 정렬하기3

import sys
input = sys.stdin.readline

num_list = [0]*10001

n = int(input())

for i in range(0, n):
    num_list[int(input())] += 1;

for i in range(1, len(num_list)):
    for j in range(0, num_list[i]):
        print(i)



# [백준 2750] 수 정렬하기

num_list = [0]*2001

n = int(input())

for i in range(0, n):
    input_num = int(input())
    if input_num >= 0:
        num_list[input_num+1000] += 1
    else:
        num_list[1000-abs(input_num)] += 1

for i in range(0, len(num_list)):
    if num_list[i] == 1:
        print(i-1000)



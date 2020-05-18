# [백준 1427] 소트인사이드

line = input()

number_count = [0]*10

for i in range(0, len(line)):
    number_count[9-int(line[i])] += 1

for i in range(0, len(number_count)):
    for j in range(0, number_count[i]):
        print(9-i, end="")

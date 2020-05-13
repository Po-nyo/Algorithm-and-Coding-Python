
# [백준_1159] 농구경기

n = int(input())
alphabet_count = [0] * 26

for i in range(0, n):
    current = input()[0]
    alphabet_count[ord(current) - ord('a')] += 1

for i in range(0, len(alphabet_count)):
    if alphabet_count[i] >= 5:
        print(chr(i+ord('a')), end="")

if max(alphabet_count) < 5:
    print("PREDAJA")
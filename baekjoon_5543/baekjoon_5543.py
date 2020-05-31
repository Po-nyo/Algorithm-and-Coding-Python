# [백준 5543] 상근날드

import sys
input = sys.stdin.readline

burger = int(input())

for i in range(0, 2):
    temp = int(input())
    if burger > temp:
        burger = temp

beverage = int(input())
temp = int(input())
if beverage > temp:
    beverage = temp

print(burger + beverage - 50)

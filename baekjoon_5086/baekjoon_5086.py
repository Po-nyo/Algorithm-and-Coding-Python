# [백준 5086] 배수와 약수

import sys


def check(a, b):
    if a < b:
        if b % a == 0:
            return "factor"
    else:
        if a % b == 0:
            return "multiple"
        else:
            return "neither"


while True:
    a, b = map(int, sys.stdin.readline().rstrip("\n").split())
    if a == 0 and b == 0:
        break
    print(check(a, b))

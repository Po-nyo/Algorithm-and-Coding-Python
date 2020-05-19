# [백준 10828] 스택
import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(0, n):
    line = input().strip()
    if line == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))
    elif line == "size":
        print(len(stack))
    elif line == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif line == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    else:
        num = int(line.replace("push ", ""))
        stack.append(num)

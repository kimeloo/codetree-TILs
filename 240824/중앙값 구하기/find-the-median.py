import sys

num = list(map(int, sys.stdin.readline().split()))

for i in num:
    if i not in [max(num), min(num)]:
        print(i)
import sys
a = int(sys.stdin.readline().strip())
num = map(int, sys.stdin.readline().split())

result = []
for n in num:
    result.append(1 if a>n else 0)
print(*result, sep="\n")
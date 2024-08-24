import sys
a = int(sys.stdin.readline().strip())
num = map(int, sys.stdin.readline().split())

result = [1 if a>n else 0 for n in num]
print(*result, sep="\n")
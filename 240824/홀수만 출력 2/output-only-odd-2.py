import sys

a, b = map(int, sys.stdin.readline().split())

print(*[i for i in range(a, b-1, -2)], sep=" ")
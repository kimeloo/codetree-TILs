import sys

a, b, c = map(int, sys.stdin.readline().split())

print(1 if (b>a)&(b<c) else 0)
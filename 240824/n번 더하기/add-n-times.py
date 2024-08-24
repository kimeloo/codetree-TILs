import sys

a, n = map(int, sys.stdin.readline().split())

for _ in range(n):
    a+=n
    print(a)
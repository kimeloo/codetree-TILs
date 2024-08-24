import sys

a, b = map(int, sys.stdin.readline().split())

print(str(a)*b if a>0 else 0)
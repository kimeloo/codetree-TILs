import sys
a, b = map(int, sys.stdin.readline().split())
if a>b:
    r = a*b
else:
    r = b//a
print(r)
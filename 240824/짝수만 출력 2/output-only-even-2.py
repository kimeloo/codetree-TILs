import sys
b, a = map(int, sys.stdin.readline().split())
while b>=a:
    print(b, end=" ")
    b-=2
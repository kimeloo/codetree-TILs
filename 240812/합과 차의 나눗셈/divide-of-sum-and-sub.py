import sys

a, b = map(int, sys.stdin.readline().split())

print('{:.2f}'.format((a+b)/(a-b)))
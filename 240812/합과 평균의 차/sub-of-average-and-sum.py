import sys
a,b,c = map(int, sys.stdin.readline().split())
s = a+b+c
a = int(s/3)
print('{}\n{}\n{}'.format(s, a, s-a))
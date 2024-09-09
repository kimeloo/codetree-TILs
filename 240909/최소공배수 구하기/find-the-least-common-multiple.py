import sys

def sim(a, b):
    while b>0:
        a, b = b, a%b
    return a

n, m = map(int, sys.stdin.readline().split())

gcd = sim(n,m)
print((n*m)//gcd)
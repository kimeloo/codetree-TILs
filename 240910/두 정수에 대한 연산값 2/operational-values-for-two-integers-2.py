import sys

def inp():
    a, b = map(int, sys.stdin.readline().split())
    return a,b
def cal(a,b):
    if a>b:
        a*=2
        b+=10
    else:
        a+=10
        b*=2
    return a, b

def main():
    a, b = inp()
    print(*cal(a,b))

main()
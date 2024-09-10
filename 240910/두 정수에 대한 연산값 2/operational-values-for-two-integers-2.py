import sys

def inp():
    a, b = map(int, sys.stdin.readline().split())
    return a,b
def cal(a,b):
    a, b = min(a,b), max(a,b)
    return a+10, b*2

def main():
    a, b = inp()
    print(*cal(a,b))

main()
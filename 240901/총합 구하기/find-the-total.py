import sys


def main():
    a, b = map(int, sys.stdin.readline().split())
    s = 0
    for n in range(a,b+1):
        if (n%6==0) and (n%8!=0):
            s += n
    print(s)

if __name__ == '__main__':
    main()
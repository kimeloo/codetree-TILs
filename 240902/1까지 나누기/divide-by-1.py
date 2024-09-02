import sys


def main():
    n = int(sys.stdin.readline().strip())
    cnt = 0
    div = 1
    while n>1:
        n = n // div
        div += 1
        cnt += 1
    print(cnt)
main()
import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    result = 1
    for n in range(1, b+1):
        if n%a==0:
            result *= n
    print(result)

main()
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        if (num % 3 == 0) and (num % 2 == 1):
            print(num)

if __name__ == '__main__':
    main()
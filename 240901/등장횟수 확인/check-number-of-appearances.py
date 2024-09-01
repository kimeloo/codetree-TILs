import sys

def main():
    cnt = 0
    for _ in range(5):
        num = int(sys.stdin.readline().strip())
        if num % 2 == 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
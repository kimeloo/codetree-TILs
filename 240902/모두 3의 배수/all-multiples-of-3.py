import sys

def main():
    for _ in range(5):
        n = int(sys.stdin.readline().strip())
        if n%3!=0:
            print(0)
    else:
        print(1)


main()
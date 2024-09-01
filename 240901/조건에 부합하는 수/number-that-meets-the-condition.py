import sys

def main():
    a = int(sys.stdin.readline().strip())
    for n in range(1, a+1):
        t1 = n//8
        t2 = n%7
        if ((n%2==0) and (n%4!=0)) or (t1%2==0) or (t2<4):
            pass
        else:
            print(n, end=" ")

main()
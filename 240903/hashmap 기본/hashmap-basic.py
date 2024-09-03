import sys

def inp():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        command(sys.stdin.readline().split())

def command(c):
    if len(c)==3:
        what, key, value = c
    else:
        what, key = c
    if what=="add":
        d[key] = value
    elif what=="find":
        if key in d:
            print(d[key])
        else:
            print("None")
    else:
        d.pop(key)

def main():
    inp()


if __name__ == '__main__':
    d = {}
    main()
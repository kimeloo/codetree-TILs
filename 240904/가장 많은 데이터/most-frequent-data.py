import sys

def main():
    n = int(sys.stdin.readline().strip())
    d = {}
    for _ in range(n):
        c = sys.stdin.readline().strip()
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    max_ = 0
    for key in d:
        if d[key] > max_:
            max_ = d[key]
    print(max_)

if __name__ == '__main__':
    main()
import sys

def inputHandler():
    n = int(sys.stdin.readline().strip())
    coinMap = []
    for _ in range(n):
        coinMap.append(list(map(int, sys.stdin.readline().split())))
    return n, coinMap

def check(n, location):
    x, y = location
    if (x-1<0) or (y-1<0) or (x+1>=n) or (y+1>=n):
        return False
    return True

def counter(coinMap, location):
    x, y = location
    count = 0
    checklist = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
    for loc in checklist:
        if coinMap[loc[1]][loc[0]] == 1:
            count += 1
    return count

def simulate(n, coinMap):
    result = []
    for i in range(n):
        for j in range(n):
            if check(n, (i,j)):
                result.append(counter(coinMap, (i,j)))
    return max(result)


def main():
    n, coinMap = inputHandler()
    print(simulate(n, coinMap))

if __name__ == '__main__':
    main()
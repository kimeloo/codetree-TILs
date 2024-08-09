import sys

def inputHandler():
    n = int(sys.stdin.readline().strip())
    numMap = []
    for _ in range(n):
        numMap.append(list(map(int, sys.stdin.readline().split())))
    return numMap

def check(numMap, location:list):
    dx = [1, -1, 0, 0]  # 동서남북
    dy = [0, 0, -1, 1]
    counter = 0
    for i in range(4):
        newX = location[0] + dx[i]
        newY = location[1] + dy[i]
        if (newX < 0) or (newY < 0):
            continue
        try:
            if numMap[newY][newX] == 1:
                counter += 1
        except:
            continue
    return counter

def main():
    numMap = inputHandler()
    result = 0
    for y, row in enumerate(numMap):
        for x, value in enumerate(row):
            if check(numMap, [x, y]) >= 3:
                result += 1
    print(result)

if __name__ == '__main__':
    main()
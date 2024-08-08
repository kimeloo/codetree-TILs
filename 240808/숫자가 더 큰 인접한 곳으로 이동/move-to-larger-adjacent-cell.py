import sys

def main():
    outputHandler(inputHandler())

def inputHandler():
    n, r, c = map(int, sys.stdin.readline().split())
    numMap = []
    for _ in range(n):
        numMap.append(list(map(int, sys.stdin.readline().split())))
    result = [numMap[r-1][c-1]]
    nextLoc = (r-1, c-1)
    while True:
        nextLoc, nextNum = findNext(nextLoc, numMap)
        if nextNum==-1:
            break
        result.append(nextNum)
    return result


def findNext(currentLoc:tuple, numMap):
    r, c = currentLoc
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        try:
            nextY = r+dy[i]
            nextX = c+dx[i]
            if nextY<0 or nextX<0:
                raise
            nextNum = numMap[nextY][nextX]
        except:
            continue
        if nextNum > numMap[r][c]:
            # print((nextY, nextX), nextNum)
            return (nextY, nextX), nextNum
    else:
        return (), -1

def outputHandler(result):
    print(*result, sep=" ")

if __name__ == '__main__':
    main()
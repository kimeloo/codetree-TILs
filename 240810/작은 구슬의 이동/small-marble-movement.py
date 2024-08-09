import sys

def inputHandler():
    n, t = map(int, sys.stdin.readline().split())
    y, x, d = sys.stdin.readline().split()
    numMap = [[0 for j in range(n+1)] for i in range(n+1)]
    return numMap, list(map(int, (y,x))), d, n, t

def check(numMap, location, direction, n):
    dy = [0, 0, -1, 1]  #동서남북
    dx = [1, -1, 0, 0]  #동서남북
    dirMap = {'R':0, 'L':1, 'D':2, 'U':3}
    newY = location[0] + dy[dirMap[direction]]
    newX = location[1] + dx[dirMap[direction]]
    if (newX < 1) or (newY < 1) or (newX > n) or (newY > n):
        return False
    return (newY, newX)

def turn(direction):
    dirMap = {'R':'L', 'L':'R', 'D':'U', 'U':'D'}
    return dirMap[direction]

def main():
    numMap, currentLoc, currentDir, n, t = inputHandler()
    while t:
        t -= 1
        checkRslt = check(numMap, currentLoc, currentDir, n)
        if checkRslt:
            currentLoc = checkRslt
        else:
            currentDir = turn(currentDir)
        # print(t, currentLoc, currentDir)
    print(*currentLoc, sep=" ")


if __name__ == '__main__':
    main()
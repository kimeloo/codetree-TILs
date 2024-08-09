import sys

def inputHandler():
    n, m = map(int, sys.stdin.readline().split())
    numMap = [[0 for i in range(m)] for j in range(n)]
    return n, m, numMap

def fill(size, numMap):
    fillNum = 1
    location = (0, 0)
    direction = 0
    numMap[location[1]][location[0]] = fillNum
    while True:
        location, direction = move(location, direction, size, numMap)
        if location:
            fillNum += 1
            numMap[location[1]][location[0]] = fillNum
        else:
            break
    return numMap



def move(curLoc, curDir, size, numMap):
    dx = [1, 0, -1, 0]  # 동남서북
    dy = [0, 1, 0, -1]
    newX = curLoc[0] + dx[curDir]
    newY = curLoc[1] + dy[curDir]
    if check((newX, newY), size, numMap):
        return (newX, newY), curDir
    else:
        curDir = (curDir + 1) % 4
        newX = curLoc[0] + dx[curDir]
        newY = curLoc[1] + dy[curDir]
        if check((newX, newY), size, numMap):
            return (newX, newY), curDir
        return False, curDir

def check(location, size, numMap):
    if (location[0] >= size[0]) or (location[1] >= size[1]) or (location[0] < 0) or (location[1] < 0):
        return False
    elif numMap[location[1]][location[0]] != 0:
        return False
    return True

def main():
    n, m, numMap = inputHandler()
    size = (m,n)
    result = fill(size, numMap)
    for _ in result:
        print(*_, sep=" ")

if __name__ == '__main__':
    main()
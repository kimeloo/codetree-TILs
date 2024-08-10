import sys

def inputHandler():
    n, m = map(int, sys.stdin.readline().split())
    numMap = [[0 for i in range(m)] for j in range(n)]
    return numMap

def check(numMap, location):
    try:
        if location[1]<0 or location[0] <0:
            pass
        elif numMap[location[1]][location[0]] == 0:
            return True
    except:
        pass
    return False

def nextCheck(numMap, location, direction):
    # 남동북서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    nextX = location[0]+dx[direction]
    nextY = location[1]+dy[direction]
    if check(numMap, (nextX, nextY)):
        return (nextX, nextY)
    return False

def findNext(numMap, location, direction):
    newLocation = nextCheck(numMap, location, direction)
    if not newLocation:
        direction = (direction + 1) % 4
        newLocation = nextCheck(numMap, location, direction)
        if not newLocation:
            return False, direction
    return newLocation, direction

def fill(numMap):
    counter = 1
    numMap[0][0] = counter
    location = (0,0)
    direction = 0
    while True:
        counter += 1
        location, direction = findNext(numMap, location, direction)
        # print(location, direction)
        if location:
            x,y = location
            numMap[y][x] = counter
        else:
            break
    return numMap

def outputHandler(result):
    for row in result:
        print(*row, sep=" ")


def main():
    numMap = inputHandler()
    outputHandler(fill(numMap))


if __name__ == '__main__':
    main()
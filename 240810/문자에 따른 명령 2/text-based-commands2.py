import sys

def direction(dirNum):
    dx = [0, 1, 0, -1]  #북동남서
    dy = [1, 0, -1, 0]
    dirNum = (dirNum+4)%4
    return (dx[dirNum], dy[dirNum])

def move(location, dirNum, char):
    if char == "L":
        dirNum -= 1
    elif char == "R":
        dirNum += 1
    else:
        moveX, moveY = direction(dirNum)
        location[0] += moveX
        location[1] += moveY

    return location, dirNum

if __name__ == '__main__':
    inputStr = sys.stdin.readline().strip()
    currDir = 0     # 북동남서
    currLoc = [0,0]
    for inputChar in inputStr:
        currLoc, currDir = move(currLoc, currDir, inputChar)
    print(*currLoc, sep=" ")
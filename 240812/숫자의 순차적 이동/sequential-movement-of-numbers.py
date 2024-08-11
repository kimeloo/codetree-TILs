import sys
from collections import deque

def inputHandler():
    n, m = map(int, sys.stdin.readline().split())
    numMap = []
    for _ in range(n):
        numMap.append(list(map(int, sys.stdin.readline().split())))
    return numMap, n, m

def locations(numMap, n):
    locMap = [i+1 for i in range(n*n)]    # 각 숫자 위치 저장할 list 생성
    for y, row in enumerate(numMap):
        for x, value in enumerate(row):
            locMap[value-1] = [locMap[value-1], (x,y)]     # [숫자, (위치)] 저장 (index이므로 -1)
    locMap = deque(locMap)
    return locMap

def check(location, n):
    x, y = location
    if x<0 or y<0 or x>=n or y>=n:
        return False
    else:
        return True

def nearMax(location, numMap, n):
    nearLocNum = []
    dx = [-1,  0,  1, -1, 1, -1, 0, 1]    # 3*3에서 1, 2, 3, 4, 6, 7, 8, 9 위치
    dy = [-1, -1, -1,  0, 0,  1, 1, 1]
    x, y = location
    for i in range(8):
        newX = x + dx[i]
        newY = y + dy[i]
        newLoc = (newX, newY)
        if check(newLoc, n):
            newNum = numMap[newY][newX]
            nearLocNum.append([newNum, newLoc])
    maxNum, maxLoc = sorted(nearLocNum, key=lambda x:-x[0])[0]
    return maxLoc, maxNum

def swapNum(numMap, currentLoc, currentNum, newLoc, newNum):
    curX, curY = currentLoc
    newX, newY = newLoc
    numMap[curY][curX] = newNum
    numMap[newY][newX] = currentNum
    return numMap

def turn(numMap, n):
    locMap = locations(numMap, n)
    override = dict()       # locations 함수로 얻은 위치가 달라진 경우 override에 저장
    while locMap:
        current, location = locMap.popleft()
        if current in override:
            location = override.pop(current)
        newLoc, newNum = nearMax(location, numMap, n)
        # print(f'override : {override}')       # debug
        # print(current, newNum, newLoc)        # debug
        # print(*numMap, sep="\n", end="\n\n")  # debug
        numMap = swapNum(numMap, location, current, newLoc, newNum)
        override[newNum] = location       # 위치가 달라졌으므로 override
    return numMap

def simulate(numMap, n, m):
    for _ in range(m):
        numMap = turn(numMap, n)
    return numMap

def outputHandler(result):
    for row in result:
        print(*row, sep=" ")

def main():
    numMap, n, m = inputHandler()
    result = simulate(numMap, n, m)
    outputHandler(result)

if __name__ == '__main__':
    main()
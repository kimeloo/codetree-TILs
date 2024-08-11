import sys

def inputHandler():
    n, m, t = map(int, sys.stdin.readline().split())
    ballMap = [[0 for i in range(n)] for j in range(n)]
    numMap = []
    for _ in range(n):
        numMap.append(list(map(int, sys.stdin.readline().split())))
    ballStart = []
    for _ in range(m):
        startXY = list(map(int, sys.stdin.readline().split()))
        startXY = [startXY[1]-1, startXY[0]-1]      # x,y 위치 바꾸고 index=0 보정
        ballStart.append(startXY)
    return ballMap, numMap, ballStart, n, t

def check(location, n):
    x, y = location
    if x<0 or y<0 or x>=n or y>=n:
        return False
    else:
        return True

def findNext(location, numMap, n):
    dx = [0, 0, -1, 1]  #상하좌우
    dy = [-1, 1, 0, 0]  #상하좌우
    x, y = location
    nearLocNum = []
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if check((newX, newY), n):
            newNum = numMap[newY][newX]
            nearLocNum.append([i, (newX, newY), newNum])    # 우선순위,좌표,숫자
    _, maxLocation, _ = sorted(nearLocNum, key=lambda x:(-x[2],x[0]))[0]   # 숫자 내림차순, 우선순위 오름차순 정렬 후 0번째 값의 좌표 저장
    return maxLocation

def moveNext(befLoc, newLoc, ballMap):
    if befLoc:
        befX, befY = befLoc
        ballMap[befY][befX] -= 1
    newX, newY = newLoc
    ballMap[newY][newX] += 1
    return ballMap

def checkCrach(ballMap):
    ballCount = 0
    for y, row in enumerate(ballMap):
        for x, value in enumerate(row):
            if value > 1:
                ballMap[y][x] = 0
            elif value == 1:
                ballCount += 1
    return ballMap, ballCount

def simulate(ballMap, numMap, locations, n, t):
    timer = -1
    while timer < t:
        newLocations = []
        for location in locations:
            if timer > -1:
                newLoc = findNext(location, numMap, n)
                befLoc = location
            else:
                newLoc = location
                befLoc = None
            ballMap = moveNext(befLoc, newLoc, ballMap)
            newLocations.append(newLoc)
        # print(*ballMap, sep="\n", end="\n\n")         # debug
        ballMap, ballCount = checkCrach(ballMap)
        locations = newLocations
        timer += 1
    return ballCount

def outputHandler(result):
    print(result)

def main():
    ballMap, numMap, locations, n, t = inputHandler()
    result = simulate(ballMap, numMap, locations, n, t)
    outputHandler(result)

if __name__ == '__main__':
    main()
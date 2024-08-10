import sys

def inputHandler():
    n = int(sys.stdin.readline().strip())
    inputList = []
    for _ in range(n):
        direction, distance = sys.stdin.readline().split()
        inputList.append((direction, int(distance)))
    return inputList

def simulate(queue):
    dirMap = {'E':0, 'W':1, 'S':2, 'N':3}     # 동서남북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    moveX, moveY = 0, 0
    time = 0
    for direction, distance in queue:
        for i in range(distance):
            moveX += dx[dirMap[direction]]
            moveY += dy[dirMap[direction]]
            time += 1
            # print(time, moveX, moveY)
            if moveX == moveY == 0:
                return time
    else:
        return False

def main():
    queue = inputHandler()
    result = simulate(queue)
    if result:
        print(result)
    else:
        print(-1)


if __name__ == '__main__':
    main()
import sys

def inputHandler():
    n = int(sys.stdin.readline().strip())
    numMap = []
    for _ in range(n):
        numMap.append(list(map(int, sys.stdin.readline().split())))
    r, c = map(int, sys.stdin.readline().split())
    return numMap, n, r, c

def blowup(numMap, n, x, y):
    num = numMap[y][x]
    for i in range(num):
        if x-i>=0:
            numMap[y][x-i] = 0
        if x+i<n:
            numMap[y][x+i] = 0
        if y-i>=0:
            numMap[y-i][x] = 0
        if y+i<n:
            numMap[y+i][x] = 0
    return numMap

def gravity(numMap, n):
    for i in range(n):
        temp = []
        for j in range(n):
            value = numMap[j][i]
            if value != 0:
                temp.append(value)
        tempCount = len(temp)
        temp = [0 for _ in range(n-tempCount)] + temp
        # print(temp)
        for j in range(n):
            numMap[j][i] = temp[j]
    return numMap

def simulate(numMap, n, x, y):
    numMap = blowup(numMap, n, x-1, y-1)
    numMap = gravity(numMap, n)
    return numMap

def outputHandler(result):
    for row in result:
        print(*row, sep=" ")

def main():
    numMap, n, y, x = inputHandler()
    numMap = simulate(numMap, n, x, y)
    outputHandler(numMap)

if __name__ == '__main__':
    main()
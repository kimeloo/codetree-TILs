import sys

def inputHandler():
    n, t = map(int, sys.stdin.readline().split())
    numList = []
    for _ in range(2):
        numList.extend(list(map(int, sys.stdin.readline().split())))
    return numList, n, t

def move(numList, n, t):
    t = (t+2*n) % (2*n)
    newList = numList[2*n-t:] + (numList[:2*n-t])
    return newList

def outputHandler(n, result):
    print(*result[:n], sep=" ")
    print(*result[n:], sep=" ")

def main():
    numList, n, t = inputHandler()
    result = move(numList, n, t)
    outputHandler(n, result)

if __name__ == '__main__':
    main()
import sys

def main():
    result = inputHandler()
    outputHandler(result)

def inputHandler():
    n = int(sys.stdin.readline().strip())
    numList = []
    for _ in range(n):
        numList.append(int(sys.stdin.readline().strip()))
    for _ in range(2):
        _range = list(map(int, sys.stdin.readline().split()))
        numList = logic(numList, _range)
    return numList

def logic(numList, _range):
    numList = numList[:_range[0]-1]+numList[_range[1]:]
    return numList

def outputHandler(result):
    print(len(result))
    print(*result, sep="\n")

if __name__ == '__main__':
    main()
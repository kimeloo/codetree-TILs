import sys

def inputHandler():
    k, n = map(int, sys.stdin.readline().split())
    return k, n

def pick(maxNum, rep, result):
    rep -= 1
    if result:
        newResult = []
        for value in result:
            newResult.append(value + " 1")
            for i in range(maxNum-1):
                newResult.append(value+" "+str(i+2))
        result = newResult
    else:
        result = [str(i+1) for i in range(maxNum)]
    if rep>0:
        result = pick(maxNum, rep, result)
    return result


def main():
    maxNum, rep = inputHandler()
    result = pick(maxNum, rep, [])
    print(*result, sep='\n')

if __name__ == '__main__':
    main()
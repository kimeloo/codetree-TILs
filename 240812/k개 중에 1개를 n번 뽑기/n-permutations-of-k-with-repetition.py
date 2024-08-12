import sys

def inputHandler():
    k, n = map(int, sys.stdin.readline().split())
    return k, n

def pick(maxNum, rep, result):
    rep -= 1
    if result:
        for idx, value in enumerate(result):
            result[idx] = value + " 1"
            for i in range(maxNum-1):
                result.append(value+" "+str(i+2))
    else:
        result = [str(i+1) for i in range(maxNum)]
    print(result)
    if rep:
        result = pick(maxNum, rep, result)
    return result


def main():
    maxNum, rep = inputHandler()
    result = pick(maxNum, rep, [])
    print(*result, sep='\n')

if __name__ == '__main__':
    main()
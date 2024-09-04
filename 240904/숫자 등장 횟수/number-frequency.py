import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = {}
    num_inp = list(map(int, sys.stdin.readline().split()))
    for num in num_inp:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1

    q_inp = list(map(int, sys.stdin.readline().split()))
    for q in q_inp:
        if q in nums:
            print(nums[q], end=" ")
        else:
            print(0, end=" ")

if __name__ == '__main__':
    main()
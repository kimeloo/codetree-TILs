import sys

def inp():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    return n, nums

def sim(i):
    if i==n:
        return
    if i%2==0:
        sorted_nums = sorted(nums[0:i+1])
        # print(i, i//2)
        # print(sorted_nums)
        print(sorted_nums[i//2], end=" ")
    sim(i+1)


n, nums = inp()
sim(0)
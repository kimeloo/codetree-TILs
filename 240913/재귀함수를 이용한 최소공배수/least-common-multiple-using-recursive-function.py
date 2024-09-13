import sys

def inp():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    return n, nums

def lcm(a, b):
    ab = a*b
    while b>0:
        a, b = b, a%b
    return ab//a

def sim():
    global nums
    if len(nums)==1:
        return nums[0]
    a = nums.pop()
    b = nums.pop()
    nums.append(lcm(a,b))
    return sim()

n, nums = inp()
print(sim())
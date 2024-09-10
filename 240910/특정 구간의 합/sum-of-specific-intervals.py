import sys

def inp():
    n, m = map(int,sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = []
    for _ in range(m):
        a1, a2 = map(int, sys.stdin.readline().split())
        b.append((a1, a2))
    return a, b

def sim(nums, rang):
    for a,b in rang:
        print(sum(nums[a-1:b]))

def main():
    a, b = inp()
    sim(a,b)

main()
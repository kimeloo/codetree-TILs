n = int(input())

nums = [i for i in range(9, 0, -1)]
p = nums.copy()
for i in range(n):
    for j in range(n):
        if len(p)<2:
            p.extend(nums)
        print(p.pop(0), end="")
    print("")
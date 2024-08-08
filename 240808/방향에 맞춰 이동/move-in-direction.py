import sys
direction = [[1,0], [-1,0], [0,-1], [0,1]]      # 동서남북
dir_match = {'E':0, 'W':1, 'S':2, 'N':3}

n = int(sys.stdin.readline().strip())
xy = [0,0]
for _ in range(n):
    _dir, _dis = sys.stdin.readline().split()
    _dis = int(_dis)
    dir_xy = direction[dir_match[_dir]]
    xy = [a+(b*_dis) for a, b in zip(xy, dir_xy)]
print(*xy, sep=" ")
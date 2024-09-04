import sys

n, m = map(int, sys.stdin.readline().split())

d = {}
cnt = 1
for _ in range(n):
    c = sys.stdin.readline().strip()
    d[c] = cnt
    d[str(cnt)] = c
    cnt += 1

for _ in range(m):
    q = sys.stdin.readline().strip()
    print(d[q])
import sys
from sortedcontainers import SortedDict

def run(cmd, a, b=None):
    if cmd == "add":
        sd[a] = b
    elif cmd == "find":
        if a in sd:
            print(sd[a])
        else:
            print(None)
    elif cmd == "remove":
        sd.pop(a)
    else:
        if sd:
            for k, v in sd.items():
                print(v, end=" ")
            print("")
        else:
            print(None)


n = int(sys.stdin.readline().strip())
sd = SortedDict()
for _ in range(n):
    inp = sys.stdin.readline().split()
    if len(inp) == 3:
        cmd, a, b = inp
        a = int(a)
    elif len(inp) == 2:
        cmd, a = inp
        a = int(a)
        b = None
    else:
        cmd = inp[0]
        a, b = None, None
    run(cmd, a, b)
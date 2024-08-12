import sys
inptstr = sorted(sys.stdin.readlines(),reverse=True)
print(*inptstr,sep='\n')
import sys
a, b = map(int, sys.stdin.readline().split())

a = a if a%2==1 else a+1

result = [i for i in range(a,b+1, 2)]
print(*result, sep=" ")
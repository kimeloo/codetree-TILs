import sys

a, b = map(int, sys.stdin.readline().split())

if a%2==1:
    a+=1
while a<=b:
    print(a, end=" ")
    a+=2
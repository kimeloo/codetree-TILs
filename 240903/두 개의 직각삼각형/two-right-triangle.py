n = int(input())

for i in range(n):
    a = "*"*(n-i)
    b = " "*i
    result = a+b+b+a
    print(result)
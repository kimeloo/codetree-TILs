n = int(input())

prev = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i%2==0:
            prev += 2
        else:
            prev += 1
        print(prev, end=" ")
    print("")
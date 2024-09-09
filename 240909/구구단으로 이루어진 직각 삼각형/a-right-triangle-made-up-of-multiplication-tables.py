n = int(input())

for i in range(n):
    result = []
    for j in range(n-i):
        result.append(f'{i+1} * {j+1} = {(i+1)*(j+1)}')
    print(*result, sep=" / ")
a,b = map(int, input().split())

for i in range(2, 9, 2):
    result = []
    for j in range(b, a-1, -1):
        result.append(f'{j} * {i} = {i*j}')
    print(*result, sep=" / ")
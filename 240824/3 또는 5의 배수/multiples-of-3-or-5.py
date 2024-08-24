a = int(input())

result = []
for n in [3,5]:
    result.append("YES" if a%n==0 else "NO")
print(*result, sep="\n")
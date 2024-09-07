n = int(input())

p = [str(i)+" " for i in range(n,0,-1)]
p.append("\n")

print(*(p*n), sep="")
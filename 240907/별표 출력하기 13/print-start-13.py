n = int(input())

cnt = 0

for row in range(2*n):
    if row%2==0:    # 홀수행
        print((n-cnt)*"* ")
    else:
        cnt += 1
        print(cnt*"* ")
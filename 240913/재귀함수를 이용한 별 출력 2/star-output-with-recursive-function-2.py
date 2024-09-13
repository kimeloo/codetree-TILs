def sim(current, n, down):
    if down:
        current -= 1
    else:
        current += 1
    if current<1:
        sim(current, n, False)
    elif current>n:
        return
    else:
        print((current)*"* ")
        sim(current, n, down)
    


n = int(input())

sim(n+1, n, True)
import sys


def inp():
    y, m, d = map(int, sys.stdin.readline().split())
    return y, m, d

def is_leap(year):
    if year%400:
        return True
    elif year%100:
        return False
    elif year%4:
        return True
    else:
        return False

def is_valid(year, month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if (1 <= day) and (day <= 31):
            return True
    elif month in [4, 6, 9, 11]:
        if (1 <= day) and (day <= 30):
            return True
    if month==2:
        if (day==29) and (is_leap(year)):
            return True
        elif (1 <= day) and (day <= 28):
            return True
    return False

def sim(y, m, d):
    seasons = {1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}
    if is_valid(y, m, d):
        if m<3:
            m += 12
        print(seasons[m//3])
    else:
        print(-1)

if __name__ == '__main__':
    y, m, d = inp()
    sim(y, m, d)
import sys

def main():
    ages = []
    while True:
        age = int(sys.stdin.readline().strip())
        if age >= 30:
            break
        ages.append(age)
    print('{:.2f}'.format(float(sum(ages)/len(ages))))





main()
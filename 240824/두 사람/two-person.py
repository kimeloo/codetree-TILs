import sys

inputs = sys.stdin.readlines()
for i in inputs:
    age, sex = i.split()
    if (int(age)>=19) & (sex=="M"):
        print(1)
        break
else:
    print(0)
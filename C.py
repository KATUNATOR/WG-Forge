n = int(raw_input())

old = []
names = []

for i in range(n):
    names.append(raw_input())

names.reverse()   

for i in names:
    if i not in old:
        print(i)
        old.append(i)

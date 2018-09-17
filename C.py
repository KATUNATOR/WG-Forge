n = int(raw_input())

old = []
names = []

for i in range(n):
    names.insert(0, raw_input())

for i in names:
    if not (i in old):
        print(i)
        old.append(i)

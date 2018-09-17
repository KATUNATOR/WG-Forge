n = int(raw_input())

names = []

for i in range(n):
    name = raw_input()
    if name in names:
        names.remove(name)
    names.insert(0, name)

for i in names:
    print(i)

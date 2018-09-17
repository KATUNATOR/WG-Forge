nm = int(raw_input())
m = map(int,raw_input().split())
m.sort()

nd = int(raw_input())
d = []
for i in range(nd):
    d.append([int(raw_input()), i])

d.sort()

print(m)
print(d)
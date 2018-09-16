from collections import deque

n = int(raw_input())

old = deque()
names = deque()

for i in range(n):
    names.appendleft(raw_input())

for i in names:
    if i not in old:
        print(i)
        old.append(i)

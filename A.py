nm = int(raw_input())
meals = sorted(int(n) for n in raw_input().split())
days = [[2 * int(raw_input()), 0] for i in xrange(int(raw_input()))]

count = 0
prew = [-1,-1]
for d in sorted(days):
    if d != prew:
        for m in meals[:]:
            if d[0] >= m:
                count += 1
                meals.remove(m)
            else:
                break
    d[1] = count
    prew = d

for i in days:
    print(i[1])
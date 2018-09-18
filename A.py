nm = int(raw_input())
meals = map(int,raw_input().split())
meals.sort()

nd = int(raw_input())
days = []
for i in range(nd):
    days.append([2 * int(raw_input()), 0])

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
    

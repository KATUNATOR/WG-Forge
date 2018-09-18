nm = int(raw_input())
meals = map(int,raw_input().split())
meals.sort()

nd = int(raw_input())
days = []
for i in range(nd):
    days.append([2 * int(raw_input()), 0])

count = 0
for d in sorted(days):
    if days.index(d) != 0 and d[0] == days[days.index(d) - 1][0]:
        d[1] = count
    else:
        for m in meals[:]:
            if d[0] >= m:
                count += 1
                meals.remove(m)
            else:
                break
        d[1] = count

for i in days:
    print(i[1])
    

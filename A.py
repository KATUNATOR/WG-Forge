nm = int(raw_input())
meals = map(int,raw_input().split())
meals.sort()

nd = int(raw_input())
days = []
for i in range(nd):
    days.append([2 * int(raw_input()), i, 0])
days.sort()

print(meals)
print(days)

count = 0

for d in days:
    if days.index(d) != 0 and d[0] != days[days.index(d) - 1][0]:
        for m in meals[:]:
            if d[0] >= m:
                count += 1
                meals.remove(m)
            else:
                break
    d[2] = count

for i in sorted(days, key = lambda day: day[1]):
    print(i[2])
    

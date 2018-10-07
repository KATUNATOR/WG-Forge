s, x, y, tb, tp, z, db = (int(n) for n in raw_input().split() + raw_input().split() + raw_input().split())

if db > 0:
	db = True
else:
	db = False

if (y > x) == db:
	rb = abs(y - z)
	if (z > x) == db:
		rb += 2 * s
else:
	if db:
		rb = 2 * s - y - z
	else:
		rb = y + z

print(min(rb * tb, abs(y - x) * tp))
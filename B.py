# s = int(input())
# x = int(input())
# y = int(input())
# tb = int(input())
# tp = int(input())
# z = int(input())
# db = int(input()) 

s = 10
x = 7
y = 3
tb = 2
tp = 3
z = 7
db = -1

if y > x:
	dp = 1
else:
	dp = -1

if dp > 0:	
	rb = y
	if db > 0:
		rb -= z
		if z > x:
			rb += 2 * s
	else:
		rb += z
	rb *= tb
	rp = (y - x) * tp
else:
	rb = s - y
	if db < 0:
		rb -= s - z
		if z < x:
			rb += 2 * s
	else:
		rb += s - z
	rb *= tb
	rp = (x - y) * tp

if rp < rb:
	print(rp)
else:
	print(rb)
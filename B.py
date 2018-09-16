# s = int(input())
# x = int(input())
# y = int(input())
# tb = int(input())
# tp = int(input())
# z = int(input())
# db = int(input()) 

s = 10
x = 3
y = 7
tb = 2
tp = 3
z = 7
db = 1

if y > x:
	dp = 1
else:
	dp = -1

if dp:	
	rb = y
	if db:
		rb -= z
		if z > x:
			rb += 2 * s
	else:
		rb += z
	rb *= tb
	rp = (y - z) * tp

print(rp)
print(rb)


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
z = 1
db = 1

if y > x:
	dp = 1
else:
	dp = -1

if dp:
	resp = (y - x) * tp
	if db:
		if z < x:
			resb = (y - z) * tb
		else:
			resb = (2 * s + y - z) * tb
	else:
		resb = (z + y) * tb

print(resp)
print(resb)
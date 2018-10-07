names = {}

for i in xrange(input()):
    name = raw_input().strip()   
    if name.isalpha() and name.islower():
        names[name] = i

for i in sorted(names.keys(), key = names.__getitem__, reverse = True):
    print(i)
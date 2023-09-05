a, b, c = 1

# ruleid: useless-if-conditional
if a:
elif a:

# ruleid: useless-if-body
if a:
else:

# a and b are different cases -- ok
if a:
elif b:


# don't report on cases like this
if a:
elif b:
elif c:
elif d:


# don't report on cases like this
if a:
elif b:
elif c:

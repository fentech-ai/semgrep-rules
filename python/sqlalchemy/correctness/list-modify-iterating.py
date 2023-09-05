l = list(range(100))
# ruleid:list-modify-while-iterate
for i in l:
    x = l.pop(0)

a = [1, 2, 3, 4]
# ruleid:list-modify-while-iterate
for i in a:
    a.pop(0)

b = [1, 2, 3, 4]
# ruleid:list-modify-while-iterate
for i in b:
    b.append(0)

c = []
# ok:list-modify-while-iterate
for i in range(5):
    c.append(i)

d = []
e = [1, 2, 3, 4]
# ok:list-modify-while-iterate
for i in e:
    d.append(i)

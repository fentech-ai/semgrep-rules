d = {"a": 1, "b": 2}
# ruleid:dict-del-while-iterate
for k, v in d.items():
    del d[k]

d = {"a": 1, "b": 2}
# ruleid:dict-del-while-iterate
for k in d.keys():
    del d[k]

# ruleid:dict-del-while-iterate
for k in d.keys():
    del d[k]

# ok:dict-del-while-iterate
for k in d.keys():
    x = d[k]

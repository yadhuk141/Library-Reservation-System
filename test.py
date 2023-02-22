a=[["y","a"],["z","b"]]
b="y"
for i in a:
        if b in i:
                a.pop(a.index(i))
print(a)
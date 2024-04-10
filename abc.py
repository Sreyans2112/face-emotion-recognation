string = " Get ready for some fun "
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))
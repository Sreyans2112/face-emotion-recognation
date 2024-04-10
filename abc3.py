str="Geeks Get Ready"
s = str.split()[::1]
print(s)
rev = ','.join(reversed(s))
print(rev)

new_str = rev.replace(',',' ',1)
print(new_str)

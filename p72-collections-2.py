import collections

c = collections.Counter('extrmely')
c['z'] = 0
print(c)
print(list(c.elements()))
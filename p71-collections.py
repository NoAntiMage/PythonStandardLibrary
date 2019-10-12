import collections

c = collections.Counter()
print('Initial: ', c)
print(type(c))

c.update('abcdaab')
print('Sequence: ' , c)

c.update({'a': 1, 'd': 5})
print('Dict : ', c)
import collections

c = collections.Counter('abcddab')

print(type(c))

for letter in 'abcde':
    print('%s : %d' %(letter, c[letter]))

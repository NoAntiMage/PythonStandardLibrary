import collections


def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='var' )
print('d: ',d )
print('foo => ', d['foo'])
print('var => ', d['bar'])

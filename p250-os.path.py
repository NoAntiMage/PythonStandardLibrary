import os.path

for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print '%15s : %s' % (path, os.path.dirname(path))
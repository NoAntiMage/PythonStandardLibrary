import os.path

for path in ['filename.txt',
             'filename',
             '/path/to/filename.txt',
             '/',
             '',
             'my-archive.tar.gz',
             'no-extensions']:
    print '%15s : %s' % (path, os.path.splitext(path))

import os
from urllib import pathname2url, url2pathname

print '-' * 50
path = '/a/b/c'
print 'Original: ', path
print 'URL: ', pathname2url(path)
print 'Path: ', url2pathname('/d/e/f')

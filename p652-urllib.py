import urllib
import os

def reporthook():
    pass

try:
    filename, msg = urllib.urlretrieve(
        'http://www.gs-robot.com'
    )
    print
    print 'File:', filename
    print 'Headers:'
    print msg
    print 'File exists before cleanup:' , os.path.exists(filename)
finally:
    urllib.urlcleanup()
    print 'File still exists: ', os.path.exists(filename)

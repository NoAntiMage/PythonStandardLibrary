import getpass

try:
    p = getpass.getpass()
except Exception, err:
    print 'ERROR: ', err
else:
    print 'You entered: ', p
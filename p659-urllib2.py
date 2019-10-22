import urllib2

r = urllib2.urlopen('http://127.0.0.1:5000/')
for line in r:
    print line.rstrip()

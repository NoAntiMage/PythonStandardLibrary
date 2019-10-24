import urllib2

r = urllib2.urlopen('http://httpbin.org/')
for line in r:
    print line.rstrip()

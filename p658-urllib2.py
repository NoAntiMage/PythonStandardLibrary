import urllib2

r = urllib2.urlopen('http://127.0.0.1:5000/')
print 'response: ', r
print 'url: ', r.geturl()

headers = r.info()
print 'date: ', headers['date']
print 'headers:'
print headers

data = r.read()
print 'length: ', len(data)
print 'data'
print data


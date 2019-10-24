import urllib

url = 'http://httpbin.org/get'
print 'urlencode(): ', urllib.urlencode({'url': url})
print 'quote(): ', urllib.quote(url)
print 'quote_plus()', urllib.quote_plus(url)
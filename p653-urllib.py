import urllib

query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = urllib.urlencode(query_args)
print 'Encoded: ', encoded_args

url = 'http://httpbin.org/?' + encoded_args
print urllib.urlopen(url).read()

import urllib
import urllib2

query_args = { 'q': 'query string', 'foo': 'bar'}
encoded_args = urllib.urlencode(query_args)
print 'Encoded: ', encoded_args

url = 'http://127.0.0.1:5000/?' + encoded_args
print urllib2.urlopen(url).read()

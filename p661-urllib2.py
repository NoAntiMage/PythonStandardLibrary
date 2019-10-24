import urllib
import urllib2

query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = urllib.urlencode(query_args)
url = 'http://httpbin.org/post'
print urllib2.urlopen(url, encoded_args).read()

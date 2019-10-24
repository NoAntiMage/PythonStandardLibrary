import urllib2

request = urllib2.Request('http://httpbin.org/')
request.add_header(
    'Uer-agent',
    'PyMOTW'
)

response = urllib2.urlopen(request)
data = response.read()
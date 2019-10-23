import socket
from urlparse import urlparse

for url in [
    'http://www.python.org',
    'https:www.mybank.com',
]:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url, port)
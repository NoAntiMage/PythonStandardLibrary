import socket

for host in ['homer', 'www', 'www.python.org', 'nosuchname']:
    try:
        print '%s : %s' % (host, socket.gethostname())
    except socket.error, err:
        print '%s : %s' % (host, err)

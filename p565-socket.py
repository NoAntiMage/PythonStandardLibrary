import socket
for host in ['wuji','www']:
    print('%6s: %s' %(host, socket.getfqdn(host)))
import socket


def get_constants(prefix):
    return dict((getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix))


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')
sock = socket.create_connection(('localhost', 8000))

print('Family: ', families[sock.family])
print('Type: ', types[sock.type])
print('Protocol: ', protocols[sock.proto])

try:
    message = 'This is the message. It will be repeated.'
    print('sending "%s"' % message)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)
finally:
    print('closing socket')
    sock.close()


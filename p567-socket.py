import socket
import urlparse

for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    print(urlparse.urlunparse(
        (socket.getservbyport(port),'wujimaster.spcae','/','','','')
        )
    )

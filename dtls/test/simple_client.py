from os import path
import ssl
from socket import socket, AF_INET, SOCK_DGRAM
from logging import basicConfig, DEBUG
basicConfig(level=DEBUG)  # set now for dtls import code
from dtls import do_patch
do_patch()

cert_path = path.join(path.abspath(path.dirname(__file__)), "certs")
s = socket(AF_INET, SOCK_DGRAM)
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_NONE, ca_certs=path.join(cert_path, "ca-cert.pem"))
ss.connect(('127.0.0.1', 28000))
ss.send('Hi there'.encode())
print(ss.recv().decode())
s = ss.unwrap()
s.close()

pass


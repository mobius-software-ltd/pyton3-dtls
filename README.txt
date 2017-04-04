# Datagram Transport Layer Security for Python

PyDTLS brings Datagram Transport Layer Security (DTLS - RFC 6347:
http://tools.ietf.org/html/rfc6347) to the Python environment. In a
nutshell, DTLS brings security (encryption, server authentication,
user authentication, and message authentication) to UDP datagram
payloads in a manner equivalent to what SSL/TLS does for TCP stream
content.

DTLS is now very easy to use in Python. If you're familiar with the
ssl module in Python's standard library, you already know how. All it
takes is passing a datagram/UDP socket to the *wrap_socket* function
instead of a stream/TCP socket. Here's how one sets up the client side
of a connection:

```
import ssl
from socket import socket, AF_INET, SOCK_DGRAM
from dtls import do_patch
do_patch()
sock = ssl.wrap_socket(socket(AF_INET, SOCK_DGRAM))
sock.connect(('foo.bar.com', 1234))
sock.send('Hi there')
```

As of version 1.2.0, PyDTLS supports DTLS version 1.2 in addition to
version 1.0. This version also introduces forward secrecy using
elliptic curve cryptography and more fine-grained configuration options.

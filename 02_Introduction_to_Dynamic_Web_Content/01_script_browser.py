import socket

# create the socket (make a phone)
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# dial the phone: connect to server if it exists and is available
my_sock.connect(('data.pr4e.org', 80))

# create a request + format the request using utf-8  using `.encode()`
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# sending the request to the server
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# close the connection ( the phone call)
my_sock.close()


'''
$ python3 01_script_browser.py
HTTP/1.1 200 OK
Date: Mon, 16 Dec 2024 17:36:23 GMT
Server: Apache/2.4.52 (Ubuntu)
Last-Modified: Mon, 15 May 2017 11:11:47 GMT
ETag: "80-54f8e1f004857"
Accept-Ranges: bytes
Content-Length: 128
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/html

<h1>The First Page</h1>
<p>
If you like, you can switch to the 
<a href="http://data.pr4e.org/page2.htm">
Second Page</a>.
</p>
'''

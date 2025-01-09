from socket import *


def create_server():
    """
    Web server logic.
    The server is awake and is waiting to respond to client's request
    """
    # make/create a socket: an endpoint
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        # specify the address and the port on which the server
        # is listening
        server_socket.bind(('localhost', 9000))

        # ask to the O.S to queue/hold the incoming call/request
        # when the server is busy responding to another client
        server_socket.listen(5)

        # start logic for a successful phone call
        while 1:
            # the server is waiting(almost indefinitely) for any phone call
            (client_socket, address) = server_socket.accept()

            # read the data from client and decode it on phone call succeed
            read_data = client_socket.recv(5000).decode()
            pieces_of_data = read_data.split("\n")
            if len(pieces_of_data) > 0:
                print(pieces_of_data[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())

            # close the connection for both server & client
            client_socket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    server_socket.close()


print('Access http://localhost:9000')
create_server()


import sys
import socket
from forward_server import server, transfer
import threading

# main function
def main():

    # port of this app. the client app should listen to this port.
    forward_port = 8888

    # the IP that server should listen to
    LOCAL_HOST = '127.0.0.1'

    # the IP that server should send packets to (which is usually localhost)
    REMOTE_HOST = '127.0.0.1'

    # get the port that server should forward packets to
    # (the port where client software is listening)
    REMOTE_PORT = int(sys.argv[1])

    MAX_CONNECTION = 0x10

    # get list of ports that this app should listen to
    local_ports = map(int, sys.argv[2:])

    # create a socket for sending packets
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # comment this line if there are problems with responds from client application.
    # but then, the port will not be static.
    remote_socket.bind(('0.0.0.0', forward_port))
    remote_socket.connect((REMOTE_HOST, REMOTE_PORT))
 
 
    # create server threads for each of listening ports
    server_threads = []
    for local_port in local_ports:
        s= threading.Thread(target=server, args=(LOCAL_HOST, local_port, REMOTE_HOST, REMOTE_PORT, MAX_CONNECTION, remote_socket))
        server_threads.append(s)

    # start server threads
    for s in server_threads:
        s.start()


# start the application
if __name__ == "__main__":
    main()

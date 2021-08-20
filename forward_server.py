import socket
import threading


# forward a packet
def transfer(src, dst):
    # start receiving data and forwarding it into the port

    # while there is still data coming
    while True:
        # get some data and put it into a buffer
        buffer = src.recv(0x400)

        # if buffer is empty, then we are done
        if len(buffer) == 0:
            print( "[-] No data received! Breaking...")
            break

        # send data into destination. which is the client application
        dst.send(buffer)

    # when finished, close the socket from internet
    src.shutdown(socket.SHUT_RDWR)
    src.close()



# server listens to a socket
# whenever a packet arrives, forwards it to the dedicated port
def server(local_host, local_port, remote_host, remote_port, max_connection, remote_socket):

    # make a server socket and start listening to dedicated IP and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((local_host, local_port))
    server_socket.listen(max_connection)

    print( '[+] Server started [%s:%d]' % (local_host, local_port))
    print( '[+] Connect to [%s:%d] to get the content of [%s:%d]' % (local_host, local_port, remote_host, remote_port))

    # start the job
    while True:

        # wait for a connection
        local_socket, local_address = server_socket.accept()
        print( '[+] Detect connection from [%s:%s]' % (local_address[0], local_address[1]))
        print( "[+] Trying to connect the REMOTE server [%s:%d]" % (remote_host, remote_port))
        print( "[+] Tunnel connected! Tranfering data...")

        # make a forwarding thread
        s = threading.Thread(target=transfer, args=(
            remote_socket, local_socket))
        r = threading.Thread(target=transfer, args=(
            local_socket, remote_socket))
        s.start()
        r.start()



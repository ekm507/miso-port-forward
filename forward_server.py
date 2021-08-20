import socket


# forward a packet
def transfer(src, dst):

    while True:
        buffer = src.recv(0x400)

        if len(buffer) == 0:
            print( "[-] No data received! Breaking...")
            break

        dst.send(buffer)

    src.shutdown(socket.SHUT_RDWR)
    src.close()


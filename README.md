# port forwarding Multi-Input-Single-Output

forward several ports into a single one 


this tool forwards packets from several ports into one single port.

# how it works:
it stays on client side before client application and forwards all packets from multiple ports into one single localhost port.  
the application that wants to receive data listens to the dedicated port on localhost.

## block diagram

![block diagram image](block-diagram.jpg)

_ascii block diagram drawn using asciiflow.com_

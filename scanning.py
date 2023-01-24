import socket


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host = input("=> Enter the IP to Scan: ")


def portscanner(port):
        if sock.connect_ex ((host,port)):
                print ("[*] Port %d is closed" % (port))
        else:
                print ("[=>] Port %d is open" %(port))

for port in range(1,1000):
        portscanner(port)

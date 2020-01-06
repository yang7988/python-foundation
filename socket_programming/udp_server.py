from socket import *
from time import ctime

HOST = ""
PORT = 9904
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(bytes(data, "utf-8"))
    print("...received from and returned to :", addr)

# udpSerSock.close()

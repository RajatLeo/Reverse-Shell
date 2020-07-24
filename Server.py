import socket
import sys


# Create Socket
def create_socket():
    try:
        global host, port, soc
        host = ""
        port = 9999
        soc = socket.socket()
        print("Socket Created on Port: " + str(port))
    except Exception as error:
        print("Socket Creation Error: " + str(error))


# Bind port and host and listen for connection
def binding():
    try:
        global host, port, soc
        print(host,port,soc)
        print("Binding Port...")
        soc.bind((host, port))
        soc.listen(5)
        print("Waiting for Connection...")
    except:
        print("Error in binding port \n Retrying...")
        binding()


# Accept connection for furthur communication
def accept_connection():
    # global soc
    while True:
        connection, address = soc.accept()
        print("Connected with " + "IP: " + str(address[0]) + "| Port:" + str(address[1]))
        command(connection)
        connection.close()
        soc.close()


def command(connection):
    try:
        while True:
            s = input()
            if s == "quit":
                connection.send(str.encode(s))
                sys.exit()
            if len(str.encode(s)) > 0:
                connection.send(str.encode(s))
                response = str(connection.recv(1024), "utf-8")
                print(response + " ")
    except Exception as e:
        print(e)
        print("Error in sending Data")


def main():
    create_socket()
    binding()
    accept_connection()


main()

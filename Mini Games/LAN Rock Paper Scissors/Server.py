import os
import socket
import sys
import threading

Host=("localhost")
Port=9090

Server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Port))
Server.listen(20)

def get_ip():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    LAN_IP=s.getsockname()[0]
    return LAN_IP

def Main():

    Clients=[]
    Players=[]
    PlayersMoved=[0,0]
    Moves=[0,0]
    Result=""
    print (Moves,PlayersMoved,Result)

    def Connections():
        while True:
            Client, Address=Server.accept()
            print("Connected with ",Address)
            Client.send('NICKNAME'.encode('ascii'))
            Player=Client.recv(1024).decode('ascii')
            Players.append(Player)
            Clients.append(Client)
            print("Nickname is ",Player)
            Broadcast(str(Player+" joined!"))
            Client.send('Connected to server!'.encode('ascii'))
            Process1=""
            Process1=threading.Thread(target=GetMoves, args=(Client,))
            Process1.start()

    def GetMoves(Client):
        while True:
            try:
                Message=Client.recv(1024).decode('ascii')
                if Message=="RESTART":
                    Broadcast("RESTART")
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

                print(Message)
                PlayerMove=""
                Parted=False
                for i in range(len(list(Message))):
                    if Message[i]==":":
                        Parted=True
                    elif not Parted:
                        PlayerMove+=list(Message)[i]
                    elif Parted:
                        Move=int(Message[i+1])
                        break

                if PlayersMoved[0]==0:
                    PlayersMoved[0]=PlayerMove
                    Moves[0]=Move
                else:
                    PlayersMoved[1]=PlayerMove
                    Moves[1]=Move
                    Process2=threading.Thread(target=Game)
                    Process2.start()

            except:
                index=Clients.index(Client)
                Clients.remove(Client)
                Client.close()
                Player=Players[index]
                Broadcast(str(Player+" left!"))
                Players.remove(Player)
                break


    def Game():
        Result=""
        # 1=Rock, 2=Paper, 3=Scissors
        if Moves[0]==1:
            if Moves[1]==1:
                Result="Tie"
            elif Moves[1]==2:
                Result=str(PlayersMoved[1]+" Won")
            elif Moves[1]==3:
                Result=str(PlayersMoved[0]+" Won")

        elif Moves[0]==2:
            if Moves[1]==2:
                Result="Tie"
            elif Moves[1]==3:
                Result=str(PlayersMoved[1]+" Won")
            elif Moves[1]==1:
                Result=str(PlayersMoved[0]+" Won")

        elif Moves[0]==3:
            if Moves[1]==3:
                Result="Tie"
            elif Moves[1]==1:
                Result=str(PlayersMoved[1]+" Won")
            elif Moves[1]==2:
                Result=str(PlayersMoved[0]+" Won")
        print(Result)
        Broadcast(Result)

    def Broadcast(Result):
        for Client in Clients:
            Client.send(str(Result).encode('ascii'))


    print ("Server is listening...")
    Connections()

Main()
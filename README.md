# Showcase
These programs are the ones noted on my CV.

Over the last year i made several programs of which the best are listed in this repository. Below i mention the description of each file.

# Hacks

Hacks is a folder which includes some tools that hackers use to gain illegal access to data from (a computer network, system, etc.). Obviously i have never used any of these tools illegaly, neither have the intension to. I made these programs for educational purposes only.

**1. BotNet**

> *«Botnets are networks of hijacked computer devices used to carry out various scams and cyberattacks. The term “botnet” is formed from the word’s “robot” and “network”. The bots serve as a tool to automate mass attacks, such as data theft, server crashing, and malware distribution.» -Kaspersky*

The folder BotNet has 3 subfolders which have tools that compile the main program which is inside the "Main Program" folder. The main program is divided in 2 scripts of which the one is the server and the other is the client.

- **A. Main Program**
  
   - Server.py

      The server script is the host that handles all conections and is normally used by the hacker, via this program the hacker has access to the infected systems and can command and operate them remotelly. Specifically the hacker has access to the connected system's Command Promt, Keyboard data, and can command the system to DoS* attack a given IP address or domain on a specific port.
  
   - C8dq5j.py

      This is the client script which infects a computer system. When opened, the script tries to find the file path to itself inside the computer's files which makes the creation and deletion of some files easier (The file name was randomly generated so it can be unique in someones system, otherwise the script could fail finding the path to itself therefore the program wouldn't be useable). Afterwards, it creates a System information file (.NFO) in a .txt format which is used to copy the computers name and set it as the connections nickname. After that, it connects immediately to the server with the, previously mentioned, nickname. At this point the server/hacker has full access to the following things:
      - Send commands and receive outputs from Windows Command Prompt.
      - Receive all keyboard keypresses from the moment the Client program was launched and forward.
      - Command system to DoS* Attack a given IP or domain on a specific port.

  - The program is also undetectable from most antiviruses including Kaspersky, Bitdefender, Avast, Malwarebytes and other popular alternatives.


- **B. DDoSAttack**

  - DDoSAttack.py 

    > *«Distributed Denial of Service (DDoS) attacks take advantage of the specific capacity limits that apply to any network resources – such as the infrastructure that enables a company’s website. The DDoS attack will send multiple requests to the attacked web resource – with the aim of exceeding the website’s capacity to handle multiple requests, and prevent the website from functioning correctly.» -Kaspersky*

    This script was created to do exactly whats mentioned above. It can send hundreds or even thousands (depending on the systems CPU and Network resources) of requests every second to a website. It also has the feature of hiding the system's real identity by sending requests through Anonymous proxies**.

- **C. KeyboardRecorder**

  - Recorder.py

    > *«Keyloggers are built for the act of keystroke logging — creating records of everything you type on a computer or mobile keyboard. These are used to quietly monitor your computer activity while you use your devices as normal. Keyloggers are used for legitimate purposes like feedback for software development but can be misused by criminals in order to gain fraudulent access to passwords and other confidential information.» -Kaspersky*

    As mentioned above this script records every key pressed on the infected machine's keyboard and sends it to the server/hacker.

- **D. WebScraper**

  - Proxies.py

    > *«Web scraping is the process of using bots to extract content and data from a website. The purpose of scraping can be analysis of information retrieved, content theft, or database filling. It extracts underlying HTML code and, with it, data stored in a database. The scraper can then replicate entire website content elsewhere.» -Karspersky / Impreva.com*

    The Proxies.py script is used in association with the DDoSAttack.py script to renew the proxies that are used in a DDoS attack. This is helpful because not all proxy servers are always online, so they need to be renewed every time manually. This script automates this process by connecting to a website named "freeproxylists.net" and downloading the HTML code in order find the proxies and renew its own proxies list. It also issolates the proxies that are anonymous or elite (which are the ones that provide anonymity to the web) and ignores the transparent ones (which don't provide anonymity).



**2. Brute_Force**

- BruteForce.py
  > *«A brute force attack uses trial-and-error to guess login info, encryption keys, or find a hidden web page. Hackers work through all possible combinations hoping to guess correctly.» -Kaspersky*

  The BruteForce.py script works by giving it a password that can contain Characters, Numbers and Symbols and then tries to find it by making all the possible combinations. Before that though the 2 .txt files*** (which contain commonly used passwords) are read to try and find a match.

**3. IPCatcher**

- IPGrabber.py
  > *«An IP grabber is a third-party service that allows internet users to generate a link for detecting the IP address of anyone. All you need to do is have your target click the link.» -makeuseof.com*

  The IPGrabber.py script has the ability to write the computer's Public IP in a file and send it to a web server through FTP (File Transfer Protocol) from where a hacker can see it.

**4. MemoryAllocationOverload**

- MemoryAllocationOverload.py
  The MemoryAllocationOverload.py script is more of a fun made tool rather than a hacker tool. It's purpose is to overload your RAM by making massive lists in python, over and over again in a loop, which make your system very laggy or even unusable. However it can be fixed with a simple system restart.




# Mini Games

The Mini Games folder includes the following:

- Guess The Number
- Hangman
- Rock Paper Scissors (LAN)


**1. Guess The Number**

- Guess The Number.py
  The Guess The Number.py script is one of my first Mini Games and is pretty simple. A random number between 1 and 100 is generated and the player tries to find it by guessing. When a wrong answer is entered the program tells the player if the correct answer is higher or lower than the answer given.

**2. Hangman**

- Hangman.py
  The Hangman.py script is the first program i made with GUI. The purpose of the game is to find the Hidden word by guessing letters or the whole word. If you make a wrong guess a Stickman part is drawn on the window. If the Stickman figure is completed the player loses.

**3. Rock Paper Scissors (LAN)**

This program was made to fuction on online mode via LAN. 2 Players in the same network connect to a server (which is also on the local network) and play. This program is also made with GUI and has a restart button which can restart the game for both players when clicked so they can play again.

- Server.py
The Server.py script is the host that handles the players moves and calculates the result (Who Won or if it was a Tie).

- Client.py
The Client.py script is the program that provides the Graphical Interface and alows the players to choose Nickname and their move (Rock,Paper or Scissors). When a player chooses a nickname or makes a move, the client program sends that data to the server to handle them.





**For clarification purposes, DDoS means Distributed Denial of Service, when it happens from one system the term **"Distributed"** makes no sense thats why its called DoS Attack*

***A proxy server is a system or router that stands between users and the internet. It performs the function of a firewall and filter and is designed to protect data and privacy. It applies rules to prevent you from having to expose your digital address to the world. Only the proxy’s IP address is visable to others. Without your personal IP address, people on the internet do not have direct access to your personal data, schedules, apps, or files.*

****The files containing the commonly used passwords where taken by the user "g0tmi1k" on github*

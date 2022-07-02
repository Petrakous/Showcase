import socket
import threading
import os
import sys
import pygame as pg


def get_ip():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("10.255.255.255", 1))
    LAN_IP=s.getsockname()[0]
    return LAN_IP




def Main():

    res = (800,800)
    Screen = pg.display.set_mode(res)
    color = (255,255,255)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    Width = Screen.get_width()
    height = Screen.get_height()
    Done = False
    Active = False
    smallfont = pg.font.SysFont('Corbel',35)
    Text1 = smallfont.render('Rock' , True , color)
    Text2 = smallfont.render('Paper' , True , color)
    Text3 = smallfont.render('Scissors' , True , color)
    Text4=smallfont.render('R' , True , color)

    Clock=pg.time.Clock()
    OtherMessages=[""]
    WonMessage=[""]
    AllMessages=[""]
    PreviousLen=len(AllMessages)
    PrintColor=(30, 30, 30)
    WonFont=pg.font.SysFont("arial", 50)
    BackgroundColor=(0, 255, 0)
    InstructionFont=pg.font.SysFont("arial", 25)
    PrintInstruction="Nickname:"
    PrintInstruction2=""
    FilledBackground2=False
    ResultFont=pg.font.SysFont("arial", 22)

    Text=""
    Color_inactive=pg.Color("lightskyblue3")
    Color_active=pg.Color("dodgerblue2")
    Color=Color_inactive
    Input_box=pg.Rect(290, 600, 140, 32)
    InputFont=pg.font.SysFont("arial", 20)
    InputDone=False
    ReceiveThreadOpen=False


    Host=("localhost")
    Port=9090


    def Receive():
        while True:
            try:
                Message=Client.recv(1024).decode('ascii')
                print (Message)
                AllMessages.append(Message)
                if Message=="NICKNAME":
                    Client.send(str(Nickname).encode('ascii'))
                elif Message=="RESTART":
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    if "Won" in Message or "Tie" in Message:
                        WonMessage.append(Message)
                    else:
                        OtherMessages.append(Message)
            except:
                print("An error occured!")
                Client.close()
                break


    def RefreshText():
        PrintWon=WonMessage[-1]
        PrintWon_box=WonFont.render(PrintWon, True, BackgroundColor, PrintColor)
        PrintWon_Rect=PrintWon_box.get_rect()
        PrintWon_Rect.center=(400, 200)
        Screen.blit(PrintWon_box, PrintWon_Rect)

        PrintNotifications=OtherMessages[-1]
        PrintNotifications_box=ResultFont.render(PrintNotifications, True, BackgroundColor, PrintColor)
        PrintNotifications_Rect=PrintNotifications_box.get_rect()
        PrintNotifications_Rect.center=(375, 550)
        Screen.blit(PrintNotifications_box, PrintNotifications_Rect)

        PrintInstruction_box=InstructionFont.render(PrintInstruction, True, BackgroundColor, PrintColor)
        PrintInstruction_Rect=PrintInstruction_box.get_rect()
        PrintInstruction_Rect.center=(210, 614)
        Screen.blit(PrintInstruction_box, PrintInstruction_Rect)

        PrintInstruction_box2=InstructionFont.render(PrintInstruction2, True, BackgroundColor, PrintColor)
        PrintInstruction_Rect2=PrintInstruction_box2.get_rect()
        PrintInstruction_Rect2.center=(375, 300)
        Screen.blit(PrintInstruction_box2, PrintInstruction_Rect2)

    def InputBox():
        WonMessage.append("ROCK PAPER SCISSORS")
        Screen.fill((30, 30, 30))
        Txt_Surface=InputFont.render(Text, True, Color)
        Width=max(200, Txt_Surface.get_width()+10)
        Input_box.w=Width
        Screen.blit(Txt_Surface, (Input_box.x+5, Input_box.y+5))
        pg.draw.rect(Screen, Color, Input_box, 2)


    while not Done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Done = True
                pg.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if Input_box.collidepoint(event.pos):
                    Active = not Active
                else:
                    Active = False
                Color = Color_active if Active else Color_inactive

            elif event.type == pg.KEYDOWN:
                if Active:
                    if event.key == pg.K_BACKSPACE:
                        Text = Text[:-1]
                    elif event.key == pg.K_RETURN:
                        Nickname=Text
                        Text = ''
                        InputDone=True
                        PrintInstruction=""
                        WonMessage.append("")

                        Client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        Client.connect((Host, Port))

                    else:
                        Text += event.unicode

            if not InputDone:
                InputBox()

            elif InputDone:
                PrintInstruction2="Choose Your Move"
                if not ReceiveThreadOpen:
                    Receive_Thread=threading.Thread(target=Receive)
                    Receive_Thread.start()
                    ReceiveThreadOpen=True
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100+150 and height/2 <= mouse[1] <= height/2+50:
                        MyMove=str(Nickname+": 1")
                        Client.send(MyMove.encode('ascii'))
                    if 300 <= mouse[0] <= 300+150 and height/2 <= mouse[1] <= height/2+50:
                        MyMove=str(Nickname+": 2")
                        Client.send(MyMove.encode('ascii'))
                    if 500 <= mouse[0] <= 500+150 and height/2 <= mouse[1] <= height/2+50:
                        MyMove=str(Nickname+": 3")
                        Client.send(MyMove.encode('ascii'))
                    
                    if 725 <= mouse[0] <= 725+50 and 25 <= mouse[1] <= 25+50:
                        Client.send("RESTART".encode('ascii'))
                        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) #or Main()


                    
            
            
                if not FilledBackground2:
                    Screen.fill((30,30,30))
                    FilledBackground2=True

                mouse = pg.mouse.get_pos()
                if len(AllMessages)!=PreviousLen:
                    Screen.fill((30,30,30))
                    PreviousLen=len(AllMessages)
                
                
                if 100 <= mouse[0] <= 100+150 and height/2 <= mouse[1] <= height/2+50:
                    pg.draw.rect(Screen,color_light,[100,height/2,150,50])
                else:
                    pg.draw.rect(Screen,color_dark,[100,height/2,150,50])

                if 300 <= mouse[0] <= 300+150 and height/2 <= mouse[1] <= height/2+50:
                    pg.draw.rect(Screen,color_light,[300,height/2,150,50])
                else:
                    pg.draw.rect(Screen,color_dark,[300,height/2,150,50])

                if 500 <= mouse[0] <= 500+150 and height/2 <= mouse[1] <= height/2+50:
                    pg.draw.rect(Screen,color_light,[500,height/2,150,50])
                else:
                    pg.draw.rect(Screen,color_dark,[500,height/2,150,50])
                

                if 725 <= mouse[0] <= 725+50 and 25 <= mouse[1] <= 25+50:
                    pg.draw.rect(Screen,color_light,[725,25,50,50])
                else:
                    pg.draw.rect(Screen,color_dark,[725,25,50,50])



                Screen.blit(Text1 , (100+40,height/2+10))
                Screen.blit(Text2 , (300+35,height/2+10))
                Screen.blit(Text3 , (500+20,height/2+10))

                Screen.blit(Text4 , (725+15,25+10))

                
                pg.display.update()


        RefreshText()
        pg.display.update()
        pg.display.flip()
        Clock.tick(60)


pg.init()

Main()

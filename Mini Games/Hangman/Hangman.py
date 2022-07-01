import pygame as pg
import time

def wait(): #wait for key press
    result=None
    import msvcrt 
    result=msvcrt.getch()
    return result

pg.init()

def Main():
    X=600
    Y=800
    PrintWon=""
    PrintResult=""
    PrintHidden=""
    PrintInstruction=""
    Awnser=""
    Word=""
    Guess=""
    PreviousGuess=""
    HiddenWord=""
    Hidden=[]
    Wrong=0
    Active=False
    Done=False
    Filled=False
    Won=False
    BackgroundColor=(0, 255, 0)
    PrintColor=(30, 30, 30)
    Screen=pg.display.set_mode((X, Y))
    pg.display.set_caption("Hangman")
    InputFont=pg.font.Font("freesansbold.ttf", 20)
    HiddenFont=pg.font.Font("freesansbold.ttf", 30)
    InstructionFont=pg.font.Font("freesansbold.ttf", 15)
    ResultFont=pg.font.Font("freesansbold.ttf", 22)
    WonFont=pg.font.Font("freesansbold.ttf", 50)
    Clock=pg.time.Clock()
    Input_box=pg.Rect(200, 570, 140, 32)
    Color_inactive=pg.Color("lightskyblue3")
    Color_active=pg.Color("dodgerblue2")
    Color=Color_inactive
    PrintTime=0
    EmptyTime=0


    def RefreshText():
        PrintWon_box=WonFont.render(PrintWon, True, BackgroundColor, PrintColor)
        PrintWon_Rect=PrintWon_box.get_rect()
        PrintWon_Rect.center=(300, 572/2)
        Screen.blit(PrintWon_box, PrintWon_Rect)

        PrintResult_box=ResultFont.render(PrintResult, True, BackgroundColor, PrintColor)
        PrintResult_Rect=PrintResult_box.get_rect()
        PrintResult_Rect.center=(300, 525)
        Screen.blit(PrintResult_box, PrintResult_Rect)

        PrintHidden_box=HiddenFont.render(PrintHidden, True, BackgroundColor, PrintColor)
        PrintHidden_Rect=PrintHidden_box.get_rect()
        PrintHidden_Rect.center=(300, 700)
        Screen.blit(PrintHidden_box, PrintHidden_Rect)

        PrintInstruction_box=InstructionFont.render(PrintInstruction, True, BackgroundColor, PrintColor)
        PrintInstruction_Rect=PrintInstruction_box.get_rect()
        PrintInstruction_Rect.center=(100, 585)
        Screen.blit(PrintInstruction_box, PrintInstruction_Rect)


    while not Done:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                Done=True
            if event.type==pg.MOUSEBUTTONDOWN:
                if Input_box.collidepoint(event.pos):
                    Active=not Active
                else:
                    Active=False
                Color=Color_active if Active else Color_inactive
            if event.type==pg.KEYDOWN and PrintResult!="You Lost":
                if Active:
                    if event.key==pg.K_RETURN:
                        if Word=="":
                            Word=Awnser
                            Awnser=""
                        elif Word!="":
                            Guess=Awnser
                            Awnser=""
                    elif event.key==pg.K_BACKSPACE:
                        Awnser=Awnser[:-1]
                    else:
                        Awnser+=event.unicode
        if Word=="":
            PrintInstruction="Enter word to find :"
        elif not Won:
            PrintInstruction="Guess a Letter or a Word :"

        if Won:
            PrintResult=""
            if PrintTime<25 or EmptyTime>=25:
                PrintTime+=1
                PrintWon="You Won"
                EmptyTime=0
            elif PrintTime>=25:
                PrintWon=""
                EmptyTime+=1
                if EmptyTime>=25:
                    PrintTime=0
                    EmptyTime=0


        if not Filled and Word!="":
            for i in range(len(Word)):
                Hidden.append("_")
            Filled=True


        if Guess in Word and Word!="":
            for i in range(len(Word)):
                if Guess==Word[i]:
                    Hidden.pop(i)
                    Hidden.insert(i,Guess)
                    if Guess!=PreviousGuess:
                        HiddenWord=""
                        for j in range(len(Hidden)):
                            HiddenWord+=Hidden[j]+" "
                        PrintHidden=HiddenWord
                        PreviousGuess=Guess
                    if "_" not in Hidden and (not Won):
                        Won=True
                elif Guess==Word:
                    Hidden=list(Word)
                    if not Won:
                        Won=True
        elif Guess!="" and (not Won):
                Wrong+=1
                Guess=""
                PrintResult="Wrong Awnser"
                

        Screen.fill((30, 30, 30))
        # Render the current text.
        Txt_Surface=InputFont.render(Awnser, True, Color)
        # Resize the box if the text is too long.
        Width=max(200, Txt_Surface.get_width()+10)
        Input_box.w=Width
        # Blit the text.
        Screen.blit(Txt_Surface, (Input_box.x+5, Input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(Screen, Color, Input_box, 2)

        pg.draw.line(Screen, (0, 0, 0),[50, 550],[50, 6], 10)
        pg.draw.line(Screen, (0, 0, 0),[50, 10],[300, 10], 10)
        pg.draw.line(Screen, (0, 0, 0),[300, 6],[300, 30], 10)

        if Wrong>=1:
            Head=pg.draw.circle(Screen, (255, 255, 255),[300, 80], 50, 3)
        if Wrong>=2:
            Torso=pg.draw.line(Screen, (0, 0, 255),[300, 130],[300, 350], 3)
        if Wrong>=3:
            LeftHand=pg.draw.line(Screen, (255, 0, 0),[300, 200],[200, 300], 3)
        if Wrong>=4:
            RightHand=pg.draw.line(Screen, (0, 255, 0),[300, 200],[400, 300], 3)
        if Wrong>=5:
            LeftLeg=pg.draw.line(Screen, (0, 255, 255),[300, 350],[200, 500], 3)
        if Wrong>=6:
            RightLeg=pg.draw.line(Screen, (255, 255, 0),[300, 350],[400, 500], 3)
            if not Won:
                PrintResult=("You Lost")


        RefreshText()
        pg.display.update()
        pg.display.flip()
        Clock.tick(30)

#if __name__ == '__main__':

pg.init()
Main()
pg.quit()
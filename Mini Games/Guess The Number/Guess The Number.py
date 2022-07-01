import random

def wait(): #wait for key press
    result=None
    import msvcrt 
    result=msvcrt.getch()
    return result

print ("Press any key to start a game")
wait()

Play="Y"

while Play=="Y":
    Number=random.randint(0,100)
    Found=None
    Guess=int(input("Guess a number between 0-100 : "))
    while Found!=True:
        if Guess>Number:
            Guess=int(input("Your Guess was too high. Guess a smaller number : "))
        elif Guess==Number:
            print ("You Guessed Right")
            Found=True
        elif Guess<Number:
            Guess=int(input("Your Guess was too low. Guess a higher number : "))
    Play=input("Play Again? [Y,N]")
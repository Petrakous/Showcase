from time import time


Txt=open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\Brute_Force\Names.txt","r")
Name=Txt.readlines()
Txt.close()

Txt=open(r"C:\Users\peter\Documents\Programming\Python\Python_Projects\Hacks\Brute_Force\Passwords.txt","r")
CommonPassword=Txt.readlines()
Txt.close()

Lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Symbol=["!","@","#","$","%","^","&","*","(",")","_","+","-","=","`","/",".",",",":",";","'","[","]","{","}","<",">","?"]
Number=["1","2","3","4","5","6","7","8","9","0"]

Character=Lowercase+Uppercase

Character_Number=Character+Number
Character_Symbol=Character+Symbol
Number_Symbol=Number+Symbol

Character_Number_Symbol=Character+Number+Symbol


def BruteForce(Password,Length):
    
    def Names(Password):
        for i in range(len(Name)):
            while (Name[i])[:-1]==Password:
                print("Found ",(Name[i])[:-1])
                End=time()
                print('Total time: %.2f seconds' % (End-Start))
                quit()

    def CommonPasswords(Password):
        for i in range(len(CommonPassword)):
            while (CommonPassword[i])[:-1]==Password:
                print("Found ",(CommonPassword[i])[:-1])
                End=time()
                print('Total time: %.2f seconds' % (End-Start))
                quit()

    def Characters(Password,Length):
        if Length==1:
            for i in range(len(Character)):
                Guess=Character[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    Guess=Character[i]+Character[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        Guess=Character[i]+Character[j]+Character[k]
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            Guess=Character[i]+Character[j]+Character[k]+Character[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
                                
        if Length==5:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            for m in range(len(Character)):
                                Guess=Character[i]+Character[j]+Character[k]+Character[l]+Character[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            for m in range(len(Character)):
                                for n in range(len(Character)):
                                    Guess=Character[i]+Character[j]+Character[k]+Character[l]+Character[m]+Character[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            for m in range(len(Character)):
                                for n in range(len(Character)):
                                    for o in range(len(Character)):
                                        Guess=Character[i]+Character[j]+Character[k]+Character[l]+Character[m]+Character[n]+Character[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            for m in range(len(Character)):
                                for n in range(len(Character)):
                                    for o in range(len(Character)):
                                        for p in range(len(Character)):
                                            Guess=Character[i]+Character[j]+Character[k]+Character[l]+Character[m]+Character[n]+Character[o]+Character[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            for m in range(len(Character)):
                                for n in range(len(Character)):
                                    for o in range(len(Character)):
                                        for p in range(len(Character)):
                                            for q in range(len(Character)):
                                                Guess=Character[i]+Character[j]+Character[k]+Character[l]+Character[m]+Character[n]+Character[o]+Character[p]+Character[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Character)):
                for j in range(len(Character)):
                    for k in range(len(Character)):
                        for l in range(len(Character)):
                            for m in range(len(Character)):
                                for n in range(len(Character)):
                                    for o in range(len(Character)):
                                        for p in range(len(Character)):
                                            for q in range(len(Character)):
                                                for r in range(len(Character)):
                                                    Guess=Character[i]+Character[j]+Character[k]+Character[l]+Character[m]+Character[n]+Character[o]+Character[p]+Character[q]+Character[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()

    def Numbers(Password,Length):
        if Length==1:
            for i in range(len(Number)):
                Guess=Number[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    Guess=Number[i]+Number[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        Guess=Number[i]+Number[j]+Number[k]
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            Guess=Number[i]+Number[j]+Number[k]+Number[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
        if Length==5:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            for m in range(len(Number)):
                                Guess=Number[i]+Number[j]+Number[k]+Number[l]+Number[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            for m in range(len(Number)):
                                for n in range(len(Number)):
                                    Guess=Number[i]+Number[j]+Number[k]+Number[l]+Number[m]+Number[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            for m in range(len(Number)):
                                for n in range(len(Number)):
                                    for o in range(len(Number)):
                                        Guess=Number[i]+Number[j]+Number[k]+Number[l]+Number[m]+Number[n]+Number[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            for m in range(len(Number)):
                                for n in range(len(Number)):
                                    for o in range(len(Number)):
                                        for p in range(len(Number)):
                                            Guess=Number[i]+Number[j]+Number[k]+Number[l]+Number[m]+Number[n]+Number[o]+Number[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            for m in range(len(Number)):
                                for n in range(len(Number)):
                                    for o in range(len(Number)):
                                        for p in range(len(Number)):
                                            for q in range(len(Number)):
                                                Guess=Number[i]+Number[j]+Number[k]+Number[l]+Number[m]+Number[n]+Number[o]+Number[p]+Number[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Number)):
                for j in range(len(Number)):
                    for k in range(len(Number)):
                        for l in range(len(Number)):
                            for m in range(len(Number)):
                                for n in range(len(Number)):
                                    for o in range(len(Number)):
                                        for p in range(len(Number)):
                                            for q in range(len(Number)):
                                                for r in range(len(Number)):
                                                    Guess=Number[i]+Number[j]+Number[k]+Number[l]+Number[m]+Number[n]+Number[o]+Number[p]+Number[q]+Number[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()

    def Symbols(Password,Length):
        if Length==1:
            for i in range(len(Symbol)):
                Guess=Symbol[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    Guess=Symbol[i]+Symbol[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        Guess=Symbol[i]+Symbol[j]+Symbol[k]
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
        if Length==5:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            for m in range(len(Symbol)):
                                Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]+Symbol[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            for m in range(len(Symbol)):
                                for n in range(len(Symbol)):
                                    Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]+Symbol[m]+Symbol[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            for m in range(len(Symbol)):
                                for n in range(len(Symbol)):
                                    for o in range(len(Symbol)):
                                        Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]+Symbol[m]+Symbol[n]+Symbol[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            for m in range(len(Symbol)):
                                for n in range(len(Symbol)):
                                    for o in range(len(Symbol)):
                                        for p in range(len(Symbol)):
                                            Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]+Symbol[m]+Symbol[n]+Symbol[o]+Symbol[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            for m in range(len(Symbol)):
                                for n in range(len(Symbol)):
                                    for o in range(len(Symbol)):
                                        for p in range(len(Symbol)):
                                            for q in range(len(Symbol)):
                                                Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]+Symbol[m]+Symbol[n]+Symbol[o]+Symbol[p]+Symbol[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Symbol)):
                for j in range(len(Symbol)):
                    for k in range(len(Symbol)):
                        for l in range(len(Symbol)):
                            for m in range(len(Symbol)):
                                for n in range(len(Symbol)):
                                    for o in range(len(Symbol)):
                                        for p in range(len(Symbol)):
                                            for q in range(len(Symbol)):
                                                for r in range(len(Symbol)):
                                                    Guess=Symbol[i]+Symbol[j]+Symbol[k]+Symbol[l]+Symbol[m]+Symbol[n]+Symbol[o]+Symbol[p]+Symbol[q]+Symbol[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()
                                                      
    def Characters_Numbers(Password,Length):
        if Length==1:
            for i in range(len(Character_Number)):
                Guess=Character_Number[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    Guess=Character_Number[i]+Character_Number[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
        if Length==5:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            for m in range(len(Character_Number)):
                                Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]+Character_Number[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            for m in range(len(Character_Number)):
                                for n in range(len(Character_Number)):
                                    Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]+Character_Number[m]+Character_Number[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            for m in range(len(Character_Number)):
                                for n in range(len(Character_Number)):
                                    for o in range(len(Character_Number)):
                                        Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]+Character_Number[m]+Character_Number[n]+Character_Number[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            for m in range(len(Character_Number)):
                                for n in range(len(Character_Number)):
                                    for o in range(len(Character_Number)):
                                        for p in range(len(Character_Number)):
                                            Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]+Character_Number[m]+Character_Number[n]+Character_Number[o]+Character_Number[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            for m in range(len(Character_Number)):
                                for n in range(len(Character_Number)):
                                    for o in range(len(Character_Number)):
                                        for p in range(len(Character_Number)):
                                            for q in range(len(Character_Number)):
                                                Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]+Character_Number[m]+Character_Number[n]+Character_Number[o]+Character_Number[p]+Character_Number[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Character_Number)):
                for j in range(len(Character_Number)):
                    for k in range(len(Character_Number)):
                        for l in range(len(Character_Number)):
                            for m in range(len(Character_Number)):
                                for n in range(len(Character_Number)):
                                    for o in range(len(Character_Number)):
                                        for p in range(len(Character_Number)):
                                            for q in range(len(Character_Number)):
                                                for r in range(len(Character_Number)):
                                                    Guess=Character_Number[i]+Character_Number[j]+Character_Number[k]+Character_Number[l]+Character_Number[m]+Character_Number[n]+Character_Number[o]+Character_Number[p]+Character_Number[q]+Character_Number[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()

    def Characters_Symbols(Password,Length):
        if Length==1:
            for i in range(len(Character_Symbol)):
                Guess=Character_Symbol[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    Guess=Character_Symbol[i]+Character_Symbol[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
        if Length==5:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            for m in range(len(Character_Symbol)):
                                Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]+Character_Symbol[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            for m in range(len(Character_Symbol)):
                                for n in range(len(Character_Symbol)):
                                    Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]+Character_Symbol[m]+Character_Symbol[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            for m in range(len(Character_Symbol)):
                                for n in range(len(Character_Symbol)):
                                    for o in range(len(Character_Symbol)):
                                        Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]+Character_Symbol[m]+Character_Symbol[n]+Character_Symbol[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            for m in range(len(Character_Symbol)):
                                for n in range(len(Character_Symbol)):
                                    for o in range(len(Character_Symbol)):
                                        for p in range(len(Character_Symbol)):
                                            Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]+Character_Symbol[m]+Character_Symbol[n]+Character_Symbol[o]+Character_Symbol[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            for m in range(len(Character_Symbol)):
                                for n in range(len(Character_Symbol)):
                                    for o in range(len(Character_Symbol)):
                                        for p in range(len(Character_Symbol)):
                                            for q in range(len(Character_Symbol)):
                                                Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]+Character_Symbol[m]+Character_Symbol[n]+Character_Symbol[o]+Character_Symbol[p]+Character_Symbol[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Character_Symbol)):
                for j in range(len(Character_Symbol)):
                    for k in range(len(Character_Symbol)):
                        for l in range(len(Character_Symbol)):
                            for m in range(len(Character_Symbol)):
                                for n in range(len(Character_Symbol)):
                                    for o in range(len(Character_Symbol)):
                                        for p in range(len(Character_Symbol)):
                                            for q in range(len(Character_Symbol)):
                                                for r in range(len(Character_Symbol)):
                                                    Guess=Character_Symbol[i]+Character_Symbol[j]+Character_Symbol[k]+Character_Symbol[l]+Character_Symbol[m]+Character_Symbol[n]+Character_Symbol[o]+Character_Symbol[p]+Character_Symbol[q]+Character_Symbol[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()

    def Numbers_Symbols(Password,Length):
        if Length==1:
            for i in range(len(Number_Symbol)):
                Guess=Number_Symbol[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    Guess=Number_Symbol[i]+Number_Symbol[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
        if Length==5:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            for m in range(len(Number_Symbol)):
                                Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]+Number_Symbol[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            for m in range(len(Number_Symbol)):
                                for n in range(len(Number_Symbol)):
                                    Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]+Number_Symbol[m]+Number_Symbol[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            for m in range(len(Number_Symbol)):
                                for n in range(len(Number_Symbol)):
                                    for o in range(len(Number_Symbol)):
                                        Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]+Number_Symbol[m]+Number_Symbol[n]+Number_Symbol[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            for m in range(len(Number_Symbol)):
                                for n in range(len(Number_Symbol)):
                                    for o in range(len(Number_Symbol)):
                                        for p in range(len(Number_Symbol)):
                                            Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]+Number_Symbol[m]+Number_Symbol[n]+Number_Symbol[o]+Number_Symbol[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            for m in range(len(Number_Symbol)):
                                for n in range(len(Number_Symbol)):
                                    for o in range(len(Number_Symbol)):
                                        for p in range(len(Number_Symbol)):
                                            for q in range(len(Number_Symbol)):
                                                Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]+Number_Symbol[m]+Number_Symbol[n]+Number_Symbol[o]+Number_Symbol[p]+Number_Symbol[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Number_Symbol)):
                for j in range(len(Number_Symbol)):
                    for k in range(len(Number_Symbol)):
                        for l in range(len(Number_Symbol)):
                            for m in range(len(Number_Symbol)):
                                for n in range(len(Number_Symbol)):
                                    for o in range(len(Number_Symbol)):
                                        for p in range(len(Number_Symbol)):
                                            for q in range(len(Number_Symbol)):
                                                for r in range(len(Number_Symbol)):
                                                    Guess=Number_Symbol[i]+Number_Symbol[j]+Number_Symbol[k]+Number_Symbol[l]+Number_Symbol[m]+Number_Symbol[n]+Number_Symbol[o]+Number_Symbol[p]+Number_Symbol[q]+Number_Symbol[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()
  
    def Characters_Numbers_Symbols(Password,Length):
        if Length==1:
            for i in range(len(Character_Number_Symbol)):
                Guess=Character_Number_Symbol[i]
                if Guess==Password:
                    print(f"Found {Guess}")
                    End=time()
                    print('Total time: %.2f seconds' % (End-Start))
                    quit()
        if Length==2:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]
                    if Guess==Password:
                        print(f"Found {Guess}")
                        End=time()
                        print('Total time: %.2f seconds' % (End-Start))
                        quit()
        if Length==3:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]
                        print(Guess)
                        if Guess==Password:
                            print(f"Found {Guess}")
                            End=time()
                            print('Total time: %.2f seconds' % (End-Start))
                            quit()
        if Length==4:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]
                            if Guess==Password:
                                print(f"Found {Guess}")
                                End=time()
                                print('Total time: %.2f seconds' % (End-Start))
                                quit()
        if Length==5:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            for m in range(len(Character_Number_Symbol)):
                                Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]+Character_Number_Symbol[m]
                                if Guess==Password:
                                    print(f"Found {Guess}")
                                    End=time()
                                    print('Total time: %.2f seconds' % (End-Start))
                                    quit()
        if Length==6:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            for m in range(len(Character_Number_Symbol)):
                                for n in range(len(Character_Number_Symbol)):
                                    Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]+Character_Number_Symbol[m]+Character_Number_Symbol[n]
                                    if Guess==Password:
                                        print(f"Found {Guess}")
                                        End=time()
                                        print('Total time: %.2f seconds' % (End-Start))
                                        quit()
        if Length==7:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            for m in range(len(Character_Number_Symbol)):
                                for n in range(len(Character_Number_Symbol)):
                                    for o in range(len(Character_Number_Symbol)):
                                        Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]+Character_Number_Symbol[m]+Character_Number_Symbol[n]+Character_Number_Symbol[o]
                                        if Guess==Password:
                                            print(f"Found {Guess}")
                                            End=time()
                                            print('Total time: %.2f seconds' % (End-Start))
                                            quit()
        if Length==8:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            for m in range(len(Character_Number_Symbol)):
                                for n in range(len(Character_Number_Symbol)):
                                    for o in range(len(Character_Number_Symbol)):
                                        for p in range(len(Character_Number_Symbol)):
                                            Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]+Character_Number_Symbol[m]+Character_Number_Symbol[n]+Character_Number_Symbol[o]+Character_Number_Symbol[p]
                                            if Guess==Password:
                                                print(f"Found {Guess}")
                                                End=time()
                                                print('Total time: %.2f seconds' % (End-Start))
                                                quit()
        if Length==9:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            for m in range(len(Character_Number_Symbol)):
                                for n in range(len(Character_Number_Symbol)):
                                    for o in range(len(Character_Number_Symbol)):
                                        for p in range(len(Character_Number_Symbol)):
                                            for q in range(len(Character_Number_Symbol)):
                                                Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]+Character_Number_Symbol[m]+Character_Number_Symbol[n]+Character_Number_Symbol[o]+Character_Number_Symbol[p]+Character_Number_Symbol[q]
                                                if Guess==Password:
                                                    print(f"Found {Guess}")
                                                    End=time()
                                                    print('Total time: %.2f seconds' % (End-Start))
                                                    quit()
        if Length==10:
            for i in range(len(Character_Number_Symbol)):
                for j in range(len(Character_Number_Symbol)):
                    for k in range(len(Character_Number_Symbol)):
                        for l in range(len(Character_Number_Symbol)):
                            for m in range(len(Character_Number_Symbol)):
                                for n in range(len(Character_Number_Symbol)):
                                    for o in range(len(Character_Number_Symbol)):
                                        for p in range(len(Character_Number_Symbol)):
                                            for q in range(len(Character_Number_Symbol)):
                                                for r in range(len(Character_Number_Symbol)):
                                                    Guess=Character_Number_Symbol[i]+Character_Number_Symbol[j]+Character_Number_Symbol[k]+Character_Number_Symbol[l]+Character_Number_Symbol[m]+Character_Number_Symbol[n]+Character_Number_Symbol[o]+Character_Number_Symbol[p]+Character_Number_Symbol[q]+Character_Number_Symbol[r]
                                                    if Guess==Password:
                                                        print(f"Found {Guess}")
                                                        End=time()
                                                        print('Total time: %.2f seconds' % (End-Start))
                                                        quit()

    Start=time()
    Names(Password)
    Start=time()
    CommonPasswords(Password)

    print("Not in commons. Input password type")

    Type=input("C,N,S,CN,CS,NS,CNS : ")

    if Type=="C":
        Start=time()
        Characters(Password,Length)
    elif Type=="N":
        Start=time()
        Numbers(Password,Length)
    elif Type=="S":
        Start=time()
        Symbols(Password,Length)
    elif Type=="CN":
        Start=time()
        Characters_Numbers(Password,Length)
    elif Type=="CS":
        Start=time()
        Characters_Symbols(Password,Length)
    elif Type=="NS":
        Start=time()
        Numbers_Symbols(Password,Length)
    elif Type=="CNS":
        Start=time()
        Characters_Numbers_Symbols(Password,Length)


Password=input("Password: ")
Length=len(Password)
BruteForce(Password,Length)


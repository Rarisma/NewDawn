#NewDawn 0.0.1 by Rarisma
#This is code to be executed by, you love, turn the tab space up, I am fired up.

System = ["0.0.1",1,0] #0 - Version, 1 - Devloper (Shows more info), 2 offical build
import time, keyboard, os
MountPoint = "" #Stores the path to the loaded game
CurrentPoint = ""
NextRoom = ""

def main(): #Function handles the main menu for NewDawn
    global MountPoint
    print("NewDawn Engine 0.0.1\n\n1) Load a game\n2) Find new games\n3) Create a game\nS) Settings\nE) Exit\n\nTo select an option press the character that is in brackets\neg; Press 1 to load a game\n")
    loop = 1
    while loop == 1:
        if keyboard.is_pressed("1"): # Checks if 1 is pressed
            
            print("Fetching game list...")
            FolderList = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\Data') #Checks Data directory for sub-directories
            print("Game list fetched!")
            
            a = 0
            while a <= len(FolderList) - 1:
                print(str(a) + ") - " + str(FolderList[a])) #prints out list of all game folders to load
                a = a + 1
            
            loop = 1
            while loop == 1: #This loop converts the input to a number and loops if it isn't
                a = input()
                try: 
                    a = int(a)
                except:
                    print("Make sure the input you entered is a number")
                else:
                    if a <= len(FolderList) - 1: # Checks that this a valid option
                        loop = 0
                    else:
                        loop = 1
            
            print("Now loading " + FolderList[a])
            MountPoint = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\" + str(FolderList[a]) #Mount Point is used internally as the path to call for the directory for the game (This is the top level and isnt set to chapter directories)
            os.system('cls')
            DawnMenu()
            
        elif keyboard.is_pressed("2"):
            print("This feature isn't available yet.")
        elif keyboard.is_pressed("3"):
            print("This feature isn't available yet.")
        elif keyboard.is_pressed("s"):
            print("This feature isn't available yet.")
        elif keyboard.is_pressed("e"):
            exit()

def DawnMenu(): # Handles the main menu for the game (Merge with real main menu?)
    global CurrentPoint
    global NextRoom
    GameProperties = ["","","","","",""] #Handles the info file and menu for the game
    a= open(MountPoint + "\\i.nfo","r")
    TempString = a.readlines()
    GameProperties[0] = TempString[0].strip()
    GameProperties[1] = TempString[1].strip()
    GameProperties[2] = TempString[2].strip()
    GameProperties[3] = TempString[3].strip()
    GameProperties[4] = TempString[4].strip()# this just reads the i.nfo file and reads and strips \n into the GameProperties variable

    print(str(GameProperties[0]) + " Ver. " + str(GameProperties[3]) + "\n\n\n1) New Game")
    if GameProperties[1] == "True": #Only displays the option to load the save if its enabled in the i.nfo file
        print("2) Load Game")
    
    print("S) Settings\nE) Exit game\nQ) Quit\n\n\nRelease Date: " + GameProperties[4])
    
    loop = 1
    while loop == 1:
        if keyboard.is_pressed("1"):
            CurrentPoint = "\\1\\"
            NextRoom = "Start\\"
            os.system("cls")
            DawnDisplay()
        elif keyboard.is_pressed("2") and GameProperties[1] == 1:
            print("Saves not implimented")
        elif keyboard.is_pressed("S"):
            print("No Settings.")
        elif keyboard.is_pressed("E"):  #Sends user back to the main menu
            main()
        elif keyboard.is_pressed("Q"):  #Makes Sure user wants to quit
            print("Hold for 3 seconds to quit...")
            time.sleep(3)
            if keyboard.is_pressed("Q"):
                quit()

def DawnDisplay():
    global CurrentPoint
    global NextRoom
    TempPath = MountPoint + CurrentPoint + NextRoom
    
    FileReader = open(TempPath + "T.txt","r") #T.txt stores text
    TempText = FileReader.readlines()    #Used to store the temporary text while its being converted
    FileReader.close()
    Text = ""
    a = 0
    while a <= len(TempText) - 1:
        Text = Text + TempText[a]
        a += 1
    Text = Text + "\n"
    
    FileReader = open(TempPath + "O.txt","r")#O.txt stores the names options
    TempText = FileReader.readlines()
    print(TempText)
    FileReader.close()

    FileReader = open(TempPath + "\\L.txt","r")#L.txt stores the path to the option rooms
    TempText2 = FileReader.readlines()
    print(TempText2                                                                                                                                 )
    FileReader.close()
    
    OptionText = ""
    Options = []
    Links = []
    a = 0
    while a <= len(TempText) - 1: #This works on the asumption Links and Options are the same length
        Options.append(TempText[a].strip())
        Links.append(TempText2[a].strip())
        a += 1

    a= 0
    print(len(Options) - 1)
    while a <= len(Options) - 1:
        print(OptionsText)
        OptionText = "\n" + str(a) + ") " + Options[a]
        a += 1

    print(str(Options) + "\n" + str(Links))

    print(Text + "\nOptions:" + OptionText)
    time.sleep(5)

main() #This is a bit of trick to force python to read all variables and functions into memory to allow functions to be called anywhere
#NewDawn Engine 0.2.0 (Python Edition)
#Your Code Wont Last - I would put the lyrics here but last time i did that my school flagged me for p**n gg smoothwall
import os, time

class System():
    #Engine Data
    tempvar = os.path.dirname(os.path.abspath(__file__)) #Only used to get the  
    SlashType = tempvar[len(tempvar) - 1] #Used for Unix Support

    #Game Data 
    Options = []
    Links = []
    EngineInfo = ["Example Game", "1", "Start", "0"]# //EngineInfo stores the locations of file  - EngineInfo {0 - Game Name 1-ChapterID, 2-RoomID, 3-OptionType (0 is over 10 options, 1 is less than 10)
    RoomPath = "" #Declares RoomPath as a global Variable

    #User Data
    TextVar = [None] * 1000
    BoolVar = [None] * 1000

class CommonCode(): #Stores Error checks and other common code

    @staticmethod #Stops linter from throwing errors since the class is only used to organise code
    def ECDataFolderCheck():
        if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\Data" == False): #Runs if \Data\ is missing
            input("Hey!\nYou are missing the Data folder!\n\nThis means you have no games downloaded.\nTo get some games please download the Data.7z on the NewDawn GitHub\n\nPress enter to quit") #Waits for the user to aknowledge the error
            exit() #Kills the game
        else:
            DataSubfolderTest = []
            for file in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\Data"):
                d = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\Data", file)
                if os.path.isdir(d):
                    DataSubfolderTest.append(os.path.basename(os.path.normpath(d)))
            if len(DataSubfolderTest) - 1 <= -1:
                print("Oh No!\nYou have no games!\nYou can download some sample games from the NewDawn Github\n\nPress enter to quit")

    @staticmethod 
    def ECCriticalFileCheck(): #Checks for O/L/T.txt files or if ChapterChange.txt exists
            if os.path.exists(System.RoomPath + "T.txt") and os.path.exists(System.RoomPath + "O.txt") and os.path.exists(System.RoomPath + "L.txt"): #Checks that all rooms exist and throws an error to check
                time.sleep(0)
            else:
                if os.path.exists(System.RoomPath + "ChapterChange.txt") == True: #Checks if a chapter Change exists
                    Temp = file.ReadAllLines(System.RoomPath + "ChapterChange.txt")
                    System.EngineInfo[1] = Temp[0]
                    System.EngineInfo[2] = "Start"
                    Engine.EngineCheck()
                else:
                    print("A Critical file is missing from this room\n If you are the developer please check that O.txt, L.txt and T.txt exists in,\n" + System.RoomPath + "\nPress enter to be sent back to the main menu\n\nSTATUS REPORT:\nT.txt is present " + os.path.exists(System.RoomPath + "T.txt") + "\nL.txt is present " + os.path.exists(System.RoomPath + "L.txt") + "\nO.txt is present " + os.path.exists(System.RoomPath + "O.txt"))
                    input()
                    Menu()
            return True

    def ECOptionsLinkCheck(self, a, b):
        if len(a) == len(b):
            pass
        else:
            input("This room is incorectly configured as it doesn't have the same lines in o.txt and l.txt\nIf you are not the developer you should report this,\n\nPress Enter to be sent back to the main menu.\n\nStatus Report:\n" + "Links:"  + str(a) + "\nOptions: " + str(b))
            Menu()
    
    @staticmethod
    def Intput(): #Sorts out input for menus
        Passback = 0
        loop = True
        while loop == True:
            try:
                Passback = int(input()) #Converts StringInput to passback (Will error if wrong)
                if Passback > 9:
                    print("Enter a number from 1-9 (Includes 0)")
                else:
                    loop = False
            except:
                print("That is not a number")
                loop = True
        return Passback

def Menu():
    print("NewDawn Engine 0.2.0 (Python Edition)\n\n1) Load Game\n0) Quit")
    Select = CommonCode.Intput()
    if Select == 1:
        os.system('cls')
        CommonCode.ECDataFolderCheck()
        print("Select a game:\n")

        #This displays all the games (Subfolders) in \Data\
        DataSubfolders = []
        for file in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\Data"):
            d = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\Data", file)
            if os.path.isdir(d):
                DataSubfolders.append(os.path.basename(os.path.normpath(d)))
        a = 1
        while len(DataSubfolders) >  a-1:
            print(str(a) + ") " + DataSubfolders[a-1])
            a = a + 1
        print("Press Enter when you are done.\n")
        time.sleep(0.5)
        
        while 1 == 1: #This loops the game permantly
            try:
                time.sleep(1)
                Select = input()
                System.EngineInfo[0] =  os.path.dirname(os.path.abspath(__file__)) + "\\" + DataSubfolders[int(Select) - 1] #gets name of game
                System.EngineInfo[1] = "1"
                System.EngineInfo[2] = "Start"
                os.system("cls")
                print(System.EngineInfo[0])
                #NewEngine.NFOMenu()
            except: #This should only be executed if there is a input that isn't a interger (or if somthing goes wrong)
                print("Please enter a valid number, Shown in brackets\nSuch as 1)") #Helpful message
Menu() #Forces python to load all the program into memory
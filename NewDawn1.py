#NewDawn 0.0.1 by Rarisma
#This is code to be executed by, you love, turn the tab space up, I am fired up like IDE.

System = ["0.0.1",1,0] #0 - Version, 1 - Devloper (Shows more info), 2 offical build
GlobeSetting = [1,0,0,0,1,0] #These are set by GlobalConfig at the master branch to stop these change System[2] from 0 to 1
import time, keyboard

def main(): #Function handles the main menu for NewDawn
    print("NewDawn Engine 0.0.1\n\n1) Load a game\n2) Find new games\n3) Create a game\nS) Settings\nE) Exit\n\nTo select an option press the character that is in brackets\neg; Press 1 to load a game\n")
    if GlobeSetting[0] != 1 and System[2] == 1: #Checks if the global kill switch is disabled and Offical build is enabled
        if GlobeSetting[4] == 1 and System[2] != 0:
            print("This build is unof6fical and will recieve no support.")
        if GlobeSetting[1] == 1 and GlobeSetting[2] != System[0]: #Checks if autoupdate is set to forced 
            print("\n\nThis version is old and it's recomended that you update.")
            AutoUpdate()
    else:
        time.sleep(0) #Makes python do nothing

    loop = 1
    while loop == 1:
        if keyboard.is_pressed("1"): # Checks if 1 is pressed
            print("Starting to load NewDawn...")
            MountPoint = "ND-NewDawn" #Set mountpoint to the game folder (Stubbed to NewDawn for now)
            Start()
        elif keyboard.is_pressed("2"):
            print("This feature isn't available yet.")
        elif keyboard.is_pressed("3"):
            print("This feature isn't available yet.")
        elif keyboard.is_pressed("s"):
            print("This feature isn't available yet.")
        elif keyboard.is_pressed("e"):
            exit()

def AutoUpdate(): #Stubbed for now but will Auto-Update the engine and possibly stories
    if GlobeSetting[3] == 1 and System[2] == 1:
        print("This build is marked unofficial and thus cannot autoupdate to prevent errors.\nPlease update manually")
        GlobeSetting = [1,0,0,0,0,0] #Stubs autoupdate
    else:
        print("Stubbed")
        GlobeSetting = [1,0,0,0,0,0] #currently stubbed to prevent loops
    main()

def Start():



main() #This is a bit of trick to force python to read all variables and functions into memory to allow functions to be called anywhere
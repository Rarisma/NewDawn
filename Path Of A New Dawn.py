Ver = "0.0.1"         #Version (Doesn't really matter but helps keep track)
Debug = 0             #Debug varaible (0-Disabled 1-Enabled)
loop = 1              #Set to anything but 1 to cause problems
Select=""             #Overwritten by player choice
#Player Variables
#Set to 1 to enable, Set to 0 to disable
Shotgun = 0           #Shotgun (Found in C2)
Keys = 1              #Keys    (Found in C2)
C3Code = 0            #Code in car (Found in C3R)
#Error codes
#Error 00- No more code to execute. (Stops program from closing when there is a error or no more code)
#Error 01- End of chapter (Like error 00 but it's confirmed not to be a error) Ironic right?
#Chapter 1 start
def C1Start():
    print("Do you know how to play? (Y/N)")
    Select = input()
    Select=Select.upper()
    if Select=="N":
        print("Things you can do are under options.")
        print("")
        C1Intro()
    elif Select=="Y":
        print("")
        C1Intro()
    elif Select == "DEBUG":
        Debug()
    else:
        C1Start()

def Debug():
    print("Welcome to debug")
    print("")
    print("Chapter 2 E")
    print("Chapter 2 R")
    print("Chapter 3 R")
    print("Chapter 3 E")
    Select = input()
    Select=Select.upper()
    if Select == "CHAPTER 2 E":
        C2EStart()
    elif Select == "CHAPTER 2 R":
        C2RStart()
    elif Select == "CHAPTER 3 R":
        C3RStart()
    elif Select == "CHAPTER 3 E":
        C3EStart()
def C1Intro():
    print("My name is lucas and I live in the lucian falls apartmant building.\nMy life is pretty average but I have a great job.\nWhat was that nightmare? And why hasn't my alarm clock woke me up?\nI'm going to be late for work\n\nOptions:\nInspect clock\nInspect plugs\nLeave bedroom")
    Select = input()
    Select=Select.upper()
    print("")
    if Select=="INSPECT PLUGS":
        C1Plugs()
    elif Select=="INSPECT CLOCK":
        C1Clock()
    elif Select=="LEAVE BEDROOM":
        C1Bedroom()
    else:
        print("invalid command")
        C1Intro()

def C1Plugs():
    print("You check the plugs.")
    print("Did the wire break?")
    print("I'll buy a new one after work.")
    print("I have 30 minutes until I have to go to work.")
    print("")
    print("Options:")
    print("Leave bedroom")
    Select = input()
    Select = Select.upper()
    print("")
    if Select=="LEAVE BEDROOM":
        C1Bedroom()
    else:
        print("Invalid command")
        C1Plugs()
		
def C1Clock():
    print("You look at the clock, it seems 30 minutes slow.")
    print("What is the current time?")
    print("It doesn't matter as you need to go to work")
    print("Work starts in 30 minutes.")
    print("")
    print("Options:")
    print("Leave bedroom")
    Select = input()
    Select=Select.upper()
    print("")
    if Select=="LEAVE BEDROOM":
        C1Bedroom()
    else:
        print("Invalid command")
        C1Plugs()

def C1Bedroom():
    print("I still have some time before I need to leave should I watch the TV or the Radio")
    print("")
    print("Options:")
    print("Watch TV")
    print("Listen to radio")
    Select = input()
    Select=Select.upper()
    print("")
    if Select=="WATCH TV":
        C1TV()
    elif Select=="LISTEN TO RADIO":
        C1Radio()
    else:
        print("Invalid command")
        C1Bedroom()

def C1Radio():
    print("You turn on the radio.")
    print("You hear somthing about a mass computer malfunction.")
    print("They then advise against using anything that relys on computers.")
    print("The audio cuts out to white noise.")
    print("")
    print("Options:")
    print("Look out the window")
    print("Leave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK OUT THE WINDOW":
        C1Window()
    elif Select == "LEAVE ROOM":
        C1Outside()
    else:
        print("Invailid command")
        C1Radio()
        
def C1TV():
    print("Most of the picture is blurred out, however the audio is clear.")
    print("It says not to use any electronics as they are malfunctioning.")
    print("All of a sudden the audio cuts off.")
    print("You wonder what to do...")
    print("")
    print("Options:")
    print("Look out the window")
    print("Leave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK OUT THE WINDOW":
        C1Window()
    elif Select == "LEAVE ROOM":
        C1Outside()
    else:
        print("Invailid command")
        C1TV()
        
def C1Window():
    print("You look out of the window.")
    print("You see a huge riot down the street.")
    print("You wonder what to do about the riot.")
    print("")
    print("Options:")
    print("Leave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C1Outside()
    else:
        print("Invailid command.")
        C1Window()
        
def C1Outside():
    print("You leave the apartment building.")
    print("You can see a group of people down the road.")
    print("You should aproach them quietly.")
    print("")
    print("Options:")
    print("Aproach the group")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "APROACH THE GROUP":
        C1Mob()
    else:
        print("Invalid command")
        C1Outside()

def C1Mob():
    print("You aproach the group of people near a car.")
    print("They are all armed unfortunetly.")
    print("However you see a gun with a suppressor.")
    print("You decide you should keep the suppressor on for now.")
    print("")
    print("Options:")
    print("Attack them")
    print("Hijack the car")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ATTACK THEM":
        C1Attack()
    elif Select == "HIJACK THE CAR":
        C1Hijack()
    else:
        print("Invalid command")
        C1Mob()

def C1Attack():
    print("You decide to attack the group.")
    print("You run to cover and shoot a guy in the leg.")
    print("The group run across the street and hide in a house.")
    print("It would probably be better to hijack the car.")
    print("")
    print("Options:")
    print("Hijack car")
    print("Attack the house")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "HIJACK CAR":
        C1Hijack()
    elif Select == "ATTACK THE HOUSE":
        print("You run towards the house and someone throws a molotov.")
        print("You die from third degree burns.")
        print("You died.")
        input("press enter to continue.")
        C1intro()
    else:
        print("Invalid command")
        C1Attack()
        
def C1Hijack():
    print("You shoot towards a house to cause a distraction.")
    print("They run into a shop.")
    print("You smash the window of the car and the keys are already there")
    print("You start the car and  get ready drive away.")
    print("")
    print("Option:")
    print("Drive away")
    print("Search car")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "DRIVE AWAY":
        C1Drive()
    elif Select == "SEARCH CAR":
        C1Search()
    else:
        print("Invalid command")
        C1Hijack()

def C1Search():
    print("You search the car and find some grenades, ammo and a crossbow bolt.")
    print("You throw the grenades in the shop.")
    print("You then get ready to drive away.")
    print("")
    print("Options:")
    print("Drive away")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "DRIVE AWAY":
        C1Drive()
    else:
        print("Invalid command")
        C1Search()


def C1Drive():
    print("You drive away.")
    print("As you leave Lucian Falls you wonder where to go.")
    print("There are 2 points listed on the satnav")
    print("The police station")
    print("The library")
    print("You wonder where to go...")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "THE POLICE STATION":
        C1Police()
    elif Select == "THE LIBRARY":
        C1Library()
    else:
        print("Invalid command")
        C1Drive()

def C1Police():
    print("You drive to the police station.")
    print("It's quite peaceful")
    print("However there as some colasped buildings.")
    print("")
    print("Options:")
    print("Enter the station")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER THE STATION":
        C1StationEnter()
    else:
        print("Invalid Command")
        C1Police()

def C1StationEnter():
    print("You enter the police station.")
    print("It's barren however there is some pasta on the desk.")
    print("It's getting late.")
    print("You decide to go to sleep.")
    print("End of chapter...")
    PATH = "1"
    print("")
    C2RStart()
    
def C1Library():
    print("You drive to the library.")
    print("Most of the buildings are untouched however some have colasped.")
    print("")
    print("Options:")
    print("Enter the library")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER THE LIBRARY":
        C1EnterLibrary()
    else:
        print("Invalid Command")
        C1Library()

def C1EnterLibrary():
    print("You enter the library")
    print("It looks abandoned.")
    print("There is some pizza on the desk.")
    print("It's getting late.")
    print("You decide to go to sleep.")
    print("")
    print("End of chapter...")
    C2EStart()
#Chapter 1 end
#Chapter 2R Start
def C2RStart():
    print("You wake up.\nYou can smell smoke...\nThe cafe is on fire!\n\nYou run and escape.\nHowever you loose the suppressor.\nYou run to the car and start to drive.\nYou decide to drive to a nearby town\n\nOptions:\nStart driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START DRIVING":
        C2RTown()
    else:
        print("Invailid Command")
        C2RStart()

def C2RTown():
    print("You drive into the town and you see a group of people\nThey try and shoot at you...\nHowever they miss.\nYou keep driving and eventually park near 2 shops.\n\nOptions:\nEnter shop\nRob shop\nPC shop\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER SHOP":
        C2RStoreChat()
    elif Select == "ROB SHOP":
        C2RRobStore()
    elif Select == "PC SHOP":
        C2RPC()
    elif Select == "LEAVE":
        C2RLeave()
    else:
        print("Invalid Command")
        C2RTown()

def C2RRobStore():
    print("You run in and shoot the shopkeeper.\nGet what you need and leave.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C2RLeave()
    else:
        print("Invalid Command")
        C2RobStore
        
def C2RStoreChat():
    print("You enter the store.\nSuprisingly the owner is still inside\nYou talk for awhile and he gives you some food and water.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C2RLeave()
    else:
        print("Invalid Command")
        C2RStoreChat()   
        
def C2RPC():
    print("You enter the PC store.\nAll of a sudden the store exploded.\nYou died...")
    input("Press enter to continue")
    C2RTown()

def C2RLeave():
    print("You get in you car and get ready to leave")
    print("You start the car and decide to drive to, Richard's house")
    print("As you get into the city the fuel indicator flashes meaning")
    print("that you will have to refuel soon.")
    print("However you can keep driving for now.")
    print("You eventually reach a fork in the road.")
    print("")
    print("Options:")
    print("Go left")
    print("Go right")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO RIGHT":
        C2RRight()
    elif Select == "GO LEFT":
        C2RLeft()
    else:
        print("Invalid Command")
        C2RLeave()
    
def C2RLeft():
    print("You drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...\n\Options:\nAttack\nGo back")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ATTACK":
        C2RAttack()
    elif Select == "GO BACK":
        C2RRight()
    else:
        print("Invalid Command")
        C2RLeave()
        
def C2RAttack():
    print("You run at them but you get shot before you can do anything.")
    print("You died...")
    input("Pres enter to restart")
    C2RTown()

def C2RRight():
    print("You start driving right.\nThis area of the city is realativly barren.\nHowever there is a building with the words dual take\nBut it seems beyond repair...\nUnexpectedly your car starts slowing down and eventually stops\n\nOptions:\nInspect car")#ちょっとなぜあなたはデュアルテイクケーキを放棄しましたか？
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "INSPECT CAR":
        C2RCar()
    else:
        print("Invalid Command")
        C2RRight()

def C2RCar():
    print("You check the car and it's definitely out of petrol.\nThere are some buildings nearby.\nYou should check nearby.\n\nOptions\nCheck house\nCheck shop")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK HOUSE":
        C2RHouse()
    elif Select == "CHECK SHOP":
        C2RShop()
    else:
        print("Invalid Command")
        C2RCar()
        
def C2RHouse():
    print("You check the house.\nThere are some keys on the shelf.\nDespite there being no cars other than yours nearby.\nYou got the Strange keys.\nHowever there is no petrol in sight.\n\nOptions:\nCheck shop")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK SHOP":
        C2RShop()
    else:
        print("Invalid Command")
        C2RHouse()

def C2RShop():
    print("You enter the shop.\nIt looks like it has been abandoned for awhile.\nHowever there are still cans of petrol and other items on the self.\nYou go back and refill the car.\n\nOptions:\nStart driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START DRIVING":
        C2RCar()
    else:
        print("Invalid Command")
        C2RShop()

def C2RCar():
    print("You see another group that have blocked the road.\nIt seems like they are waiting to hijack a car.\nWhat should you do?\n\nOptions:\nSneak through\nDrive through")
    if Shotgun == 1:
        print("Use Shotgun")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SNEAK THROUGH":
        C2RSneak()
    elif Select == "DRIVE THROUGH":
        C2RRam()
    elif Select == "USE SHOTGUN" and Shotgun == 1:
        C2RShotgun()
    else:
        print("Invalid Command")
        C2RCar()

def C2RLeft():
    print("You drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...")
    print("Options:\nAttack\nGo back")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ATTACK":
        C2RAttack()

def C2RRam():
    print("Your car has run out of fuel.\nYou try restarting the car but you are noticed.\nYou get shot\nYou died.")
    input("Press enter to restart")
    C2RShop()

def C2RShotgun():
    print("You sneak up and shoot them with shotgun.\nYou break the barricade and you can keep driving.\n\nOptions\nKeep driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP DRIVING":
        C2RKeepDriving()
    else:
        print("Invalid Command")
        C2RShotgun()
        
def C2RSneak():
    print("You sneak arround them but you have to ditch the car and everything in it.\nYou will need to find another car...\n\nOptions:\nLook around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C2RFindCar()
    else:
        print("Invalid Command")
        C2RSneak()

def C2RFindCar():
    print("You look arround and you see a car thats abandoned.\nYou jump and start the car.\nou can now continue driving.\n\nOptions:\nKeep driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP DRIVING":
        C2RKeepDriving()
    else:
        print("Invalid Command")
        C2RFindCar()

def C2RKeepDriving():
    print("You keep driving.")
    print("You are almost at Richards's appartment.")
    print("As you get closer you see signs that are displaying a countdown.")
    print("You wonder what they mean.")
    print("")
    print("Options:")
    print("Drive")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "DRIVE":
        C2REND()
    else:
        print("Invalid Command")
        C2RKeepDriving()

def C2REND():
    print("You knock on the door and the timers reach 0.")
    print("She says the countdown is about to reach 0.")
    print("You ask about what she means.")
    print("She says it has been hacked and is about to launch")
    print("You hear a rocket launch.")
    print("You run back to your car and start driving.")
    print("After arriving someone pulls you inside of a building.")
    print("End of chapter...")
    C3RStart()
#Chapter 2R End
#Chapter 2E Start
def C2EStart():
    print("You wake up.\nYou can smell smoke...\nThe building is on fire!\n\nYou run and escape.\nYou run to the car and start to drive.\nYou decide to drive to a nearby town\n\nOptions:\nStart driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START DRIVING":
        C2ETown()
    else:
        print("Invailid Command")
        C2EStart()

def C2ETown():
    print("You drive into the town and you see a group of people\nThey try and shoot at you...\nHowever they miss.\nYou keep driving and eventually park near 2 shops.\n\nOptions:\nEnter shop\nRob shop\nPC shop\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER SHOP":
        C2EStoreChat()
    elif Select == "ROB SHOP":
        C2ERobStore()
    elif Select == "PC SHOP":
        C2EPC()
    elif Select == "LEAVE":
        C2ELeave()
    else:
        print("Invalid Command")
        C2ETown()

def C2ERobStore():
    print("You run in and point the pistol at the shop keeper however he shoots you.")
    Select = input("You died press enter to restart")
    C2ETown()

        
def C2EStoreChat():
    print("You enter the store.\nSuprisingly the owner is still inside\nYou talk for awhile and he gives you some food and water.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C2ELeave()
    else:
        print("Invalid Command")
        C2EStoreChat()   
        
def C2EPC():
    print("You enter the PC store.\nAll of a sudden the store exploded.\nYou died...")
    input("Press enter to continue")
    C2ETown()

def C2ELeave():
    print("You get in you car and get ready to leave")
    print("You start the car and decide to drive to Emma's house")
    print("As you get into the city the fuel indicator flashes meaning")
    print("that you will have to refuel soon.")
    print("However you can keep driving for now.")
    print("You eventually reach a fork in the road.")
    print("")
    print("Options:")
    print("Go left")
    print("Go right")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO RIGHT":
        C2ERight()
    elif Select == "GO LEFT":
        C2ELeft()
    else:
        print("Invalid Command")
        C2ELeave()
    
def C2ELeft():
    print("You drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...\n\Options:\nAttack\nGo back")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ATTACK":
        C2EAttack()
    elif Select == "GO BACK":
        C2ERight()

def C2EAttack():
    print("You run at them but you get shot before you can do anything.")
    print("You died...")
    input("Pres enter to restart")
    C2ETown()

def C2ERight():
    print("You start driving right.\nThis area of the city is realativly barren.\nHowever there is a building with the words dual take\nBut it seems beyond repair...\nUnexpectedly your car starts slowing down and eventually stops\n\nOptions:\nInspect car")#ちょっとなぜあなたはデュアルテイクケーキを放棄しましたか？
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "INSPECT CAR":
        C2ECar()
    else:
        print("Invalid Command")
        C2ERight()

def C2ECar():
    print("You check the car and it's definitely out of petrol.\nThere are some buildings nearby.\nYou should check nearby.\n\nOptions\nCheck house\nCheck shop")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK HOUSE":
        C2EHouse()
    elif Select == "CHECK SHOP":
        C2EShop()
    else:
        print("Invalid Command")
        C2ECar()
        
def C2EHouse():
    print("You check the house.\nThere are some keys on the shelf.\nDespite there being no cars other than yours nearby.\nYou got the Strange keys.\nHowever there is no petrol in sight.\n\nOptions:\nCheck shop")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK SHOP":
        C2EShop()
    else:
        print("Invalid Command")
        C2EHouse()

def C2EShop():
    print("You enter the shop.\nIt looks like it has been abandoned for awhile.\nHowever there are still cans of petrol and other items on the self.\nYou go back and refill the car.\n\nOptions:\nStart driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START DRIVING":
        C2ECar()
    else:
        print("Invalid Command")
        C2EShop()

def C2ECar():
    print("You see another group that have blocked the road.\nIt seems like they are waiting to hijack a car.\nWhat should you do?\n\nOptions:\nSneak through\nDrive through")
    if Shotgun == 1:
        print("Use Shotgun")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SNEAK THROUGH":
        C2ESneak()
    elif Select == "DRIVE THROUGH":
        C2ERam()
    elif Select == "USE SHOTGUN" and Shotgun == 1:
        C2EShotgun()
    else:
        print("Invalid Command")
        C2ECar()

def C2ELeft():
    print("You drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...")
    print("Options:\nAttack\nGo back")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ATTACK":
        C2EAttack()

def C2ERam():
    print("You walk you towards the baricade but you are surrounded\nThe car is destroyed and the crash kills you.\nYou died.")
    input("Press enter to restart")
    C2EShop()

def C2EShotgun():
    print("You sneak up and shoot them with shotgun.\nYou break the barricade and you can keep driving.\n\nOptions\nKeep driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP DRIVING":
        C2EKeepDriving()
    else:
        print("Invalid Command")
        C2EShotgun()
        
def C2ESneak():
    print("You sneak arround them but you have to ditch the car and everything in it.\nYou will need to find another car...\n\nOptions:\nLook around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C2EFindCar()
    else:
        print("Invalid Command")
        C2ESneak()

def C2EFindCar():
    print("You look arround and you see a car thats abandoned.\nYou get in and start the car.\nou can now continue driving.\n\nOptions:\nKeep driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP DRIVING":
        C2EKeepDriving()
    else:
        print("Invalid Command")
        C2EFindCar()

def C2EKeepDriving():
    print("You keep driving.")
    print("You are almost at Emmas's appartment.")
    print("As you get closer you see signs that are displaying a countdown.")
    print("You wonder what they mean.")
    print("")
    print("Options:")
    print("Drive")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "DRIVE":
        C2EEND()
    else:
        print("Invalid Command")
        C2EKeepDriving()

def C2EEND():
    print("You knock on the door and the timers reach 0.")
    print("She says the countdown is about to reach 0.")
    print("You ask about what she means.")
    print("She says it has been hacked and is about to launch")
    print("You hear a rocket launch.")
    print("End of chapter...")
    C3EStart()
#Chapter 2E End
#Chapter 3R Start
def C3RStart():
    print("You feel someone dragging you into a building.\nYou can see a dimly lit sign saying Lucian Nuclear Shelter.\n\nAs you wakeup you hear multiple people talking about Richard.\nAs you look around someone calls your name.\nOptions:\nStand up")    
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "STAND UP":
        C3RStand()
    else:
        print("Invalid Command")
        C3RStart()
        
def C3RStand():
    print("You stand up and look around and you see that you are in a small room\nYou see that many people look shocked.\n\nAfter a couple of minutes a security guard enters.\nHe annouces that the building is on lockdown.\nHe then says that it's because of the rocket.\nOptions:\nAsk questions\nStay silent")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ASK QUESTIONS":
        C3RSQuestions()
    elif Select == "STAY SILENT":
         C3RSSilence()
    else:
        print("Invalid Command")
        C3RStand()

def C3RSSilence():
    print("You decide to stay silent.\nHowever you wonder what happened to Richard.\nYou sit there and wonder what to do next.\n\nOptions:\nWait")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WAIT":
        C3RSSirens()
    else:
        print("Invalid Command")
        C3RSSilence()

def C3RSQuestions():
    print("You wonder what to ask the security officer.\nMultiple questions\n\nOptions:\n\nWhat happened\nWhere is Richard\nWhere are we\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WHERE ARE WE":
        C3RSQLocation()
    elif Select == "WHAT HAPPENED":
        C3RSQRocket()
    elif Select == "WHERE IS RICHARD?":
        C3RSQRichard()
    elif Select == "LEAVE":
        C3RSSirens()
    else:
        print("Invalid Command")
        C3RSQuestions()

def C3RSQLocation():
    print("You asked him where we are.\nHe says you are in the towns nuclear shelter due to a hijacking.\nHe stops then continues with him explaining how it seems that technology is malfunctioning.\n\nOptions:\nAsk another question\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ASK ANOTHER QUESTION":
        C3RSQuestions()
    elif Select == "LEAVE":
        C3RSSirens()
    else:
        print("Invalid Command")
        C3RSQLocation()


def C3RSQRichard():
    print("You asked about Richard.\nHe looks around and says he was here a moment ago.\nSomeone taps you on the shoulder and wispers that Richard dragged you in there and then disapears.\nHe walks away and sits back down/\nYou think to yourslef that Richard must be in here somewhere.\n\nOptions:\nAsk another question\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ASK ANOTHER QUESTION":
        C3RSQuestions()
    elif Select == "LEAVE":
        C3RSSirens()
    else:
        print("Invalid Command")
        C3RSQRichard()
        
def C3RSQRocket():
    print("You asked him what happened?\nHe looks at you strangely and explains that all technolgy has seemingly failed.\nHe then says he knows nothing else.\nSomeone bumps into and discretly hands you a note\nIt's hard to read but it says Launch went wrong.\n\nOptions:\nAsk another question\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ASK ANOTHER QUESTION":
        C3RSQuestions()
    elif Select == "LEAVE":
        C3RSSirens()
    else:
        print("Invalid Command")
        C3RSQRocket()
 
    
def C3RSSirens():
    print("You decide to walk around but all of a sudden you hear loud sirens.\nSomeone shouts get down.\nYou hear metal being crushed.\nThen the roof colaspes...\n\nOptions:\nLook up")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK UP":
        C3RSLook()
    else:
        print("Invalid Command")
        C3RSSirens()

def C3RSLook():
    print("You hear people shouting hysterically.\nYou open your eyes and you move the rubble off of your legs.\nAfter awhile of looking around you realise that the enterance has completely colapsed!\nThere is some light coming from the lower floors.\nYou quickly climb down the stairs and you see that a wall has caved in.\n\nOptions:\nEnter cave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER CAVE":
        C3RCave()
    else:
        print("Invalid Command")
        C3RSLook()

def C3RCave():
    print("You walk into the cave and after walking for awhile you eventually find yourself in a huge crater.\nAs you walk out into the crater a small group follows you.\nYou decide to wait for the group to catch up with you.\n\nAfter looking around for some time you see a faint outline of a building.\n\nOptions:\nConsult group")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CONSULT GROUP":
        C3RConsult()
    else:
        print("Invalid Command")
        C3RCave()

def C3RConsult():
    print("You decide you wait for the group to catch up.\nYou then decide to ask them a myriad of questions.\nYou asked about the rocket\nThey said it was almost ready to launch but it was hijacked\nYou also ask them about Richard\nHowever the don't know about his disapearance.\n\nOptions:\nKeep talking\nStart walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP TALKING":
        C3RCTalk()
    elif Select == "START WALKING":
        C3RWalk()
    else:
        print("Invalid Command")
        C3RConsult()


def C3RCTalk():
    print("You decide to keep asking questions.\nYou ask about the shelter colasping.\nThey all looked confused,\nSomeone says it was blown up but someone contradicts him saying it was just improperly built.\n\nYou are now even more confused about what happened however you have to keep moving on.\n\nOptions:\nStart walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START WALKING":
        C3RWalk()
    else:
        print("Invalid Command")
        C3RCTalk()


def C3RWalk():
    print("You start walking ahead and some start to follow you.\nAwhile passes and nothing really happens but someone starts asking if you are going to go back into the building.\nOther than that nothing eventful has happened.\n\nOptions:\nKeep walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP WALKING":
        C3RKWalk()
    else:
        print("Invalid Command")
        C3RConsult()

def C3RKWalk():
    print("You Eventually find somthing noticable, A car that is partially crushed by some rubble.\nSome geologists are crowing around the rubble\The others are just looking at the car.\n\nOptions:\nObserve Rubble\nLook at car\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "OBSERVE RUBBLE":
        C3RCRubble()
    elif Select == "LOOK AT CAR":
        C3RCCar()
    elif Select == "LEAVE":
        C3RLeave()
    else:
        print("Invalid Command")
        C3RKWalk()

def C3RCCar():
    print("You look at the car door.\nThere is't much however there are some numbers scratched into the dashboard\n2038\nYou decide to remeber the code\nBesides a oil leak there isn't much here.\n\nOptions:\nLeave")
    C3Code = 1
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C3RLeave()
    else:
        print("Invalid Command")
        C3RCCar()

def C3RCRubble():
    print("You go to the back of the car and you see some people looking at the rocks.\nYou don't get whats so intresting however some people conclude that we are underground.\n\nOptions\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C3RLeave()
    else:
        print("Invalid Command")
        C3RCRubbleCnh()

def C3RLeave():
    print("You decide to keep walking...\nThen someone shouts they see a house.\nAfter looking for awhile you can see a faint outline of a house.\nAs you get closer you see some more buildings.\n\nOptions:\nAbandoned town")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ABANDONED TOWN":
        C3RTown()
    else:
        print("Invalid Command")
        C3RLeave()

def C3RTown():
    print("You aproach the dillapadated town and you see that many of the doors and windows are covered with a metal meshes or a borded up with wood.\nThe village looks to be from a couple of decades ago.\nDespite this some of the wood is weak and could be smashed.\n\nOptions:\nPrison\nHouse")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "PRISON":
         C3RPrison()
    elif Select == "HOUSE":
        C3RTHouse()
    else:
        print("Invalid Command")
        C3RTown()

def C3RTHouse():
    print("You enter the damaged house.\nSome of the doorways have collsaped.\nHowever you can still enter some of the rooms\n\nOptions:\nMain room\nKitchen\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "MAIN ROOM":
        C3RTHRoom()
    elif Select == "KITCHEN":
        C3RTHKitchen()
    elif Select == "LEAVE":
        C3RTown()
    else:
        print("Invalid Command")
        C3RTHouse()

def C3RTHRoom():
    print("You enter the main room.\nIt's mostly empty as it looks like most of the room has been set on fire.\nAbove the fireplace there's a buisness card.\n\nMost of the text has been redacted by a marker.\n\nOptions:\nKitchen\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KITCHEN":
        C3RTHKitchen()
    elif Select == "LEAVE":
        C3RTown()
    else:
        print("Invalid Command")
        C3RTHRoom()

def C3RTHKitchen():
    print("You enter the kitchen.\nThe room is completly empty but the light is turned on.\nAs you look around you start to hear leaves russeling.\nYou decide to leave...")
    C3RTown()

def C3RPrison():
    print("You enter the abandoned prison.\nThe doors look like they have been lockpicked.\nYou follow the doors and you see someone standing there in the dark.\nEND OF CHAPTER.")
#End of C3R
#Start of C3E
def C3EStart():
    print("You enter Emma's house.\nIt's quite large for a house in the woods.\nThe countdowns are at 0 and the rocket is about to launch...\nSuddenly the ground momentarily shakes\n\nDid the rocket launch?\nEmma leads you down to the basement.\n\nOptions:\nEnter basement")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER BASEMENT":
        C3EBasement()
    else:
        print("Invalid Command")
        C3EStart()

def C3EBasement():
    print("You quickly run down to the basement.\nIt's very dark but Emma quickly finds the light switch.\n\nYou look around and the room is quite barren.\nHowever the back wall is filled with shelves.\nEmma finds two chairs and you both sit down.\n\nOptions:\nLook around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C3EBLook()
    else:
        print("Invalid Command")
        C3EBasement()    

def C3EBLook():
    print("After awhile you both get bored of talking and Emma brings out two boxes.\nThey are both board games.\nHippos and the other is Checkers.\n\nWhich game should you play?\nHippo\nCheckers")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "HIPPO":
        C3EBGHippo()
    elif Select == "CHECKERS":
        C3EBGCheckers()
    else:
        print("Invalid Command")
        C3EBLook()

def C3EBGHippo():
    print("You decide to play hippos.\nEmma puts checkers back and you open the box and read the rules.\nThe corners of the rules card seem to be faded.\nThe card just says you have to collect as many fish as possible.\n\nYou play a couple of rounds but you only win 1 round.\nEmma says she is the Hippo Master.\n\nQuite a bit of time has passed.\nMaybe you can go outside now.\n\nOptions:\nPlay again\nGo outside")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "PLAY AGAIN":
        C3EBGHippo()
    elif Select == "GO OUTSIDE":
        C3BLeave()
    else:
        print("Invalid Command")
        C3EBGHippo()

def C3EBGCheckers():
    print("You decide to play checkers.\nYou are very skilled.\You put the hippo game back while Emma opens the box and reads the rules.\n\nYou played a couple of matches and you won every match except one.\nYou are the checkers master...\n\nQuite a bit of time has passed.\nMaybe you can go outside now?\n\nOptions:\nPlay again\nGo outside")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "PLAY AGAIN":
        C3EBGCheckers()
    elif Select == "GO OUTSIDE":
        C3BLeave()
    else:
        print("Invalid Command")
        C3EBGCheckers()


def C3BLeave():
    print("You decide to leave the basement.\nHowever someone has just smashed the basement door in.\nYou hide behind some of the shelves and Emma pulls out a gun and tells you to remove your supressor.\n\nYou lost the suppressor.\n\nOption:\nCover\nShoot back")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "COVER":
        C3EBCover()
    elif Select == "SHOOT BACK":
        C3EBShoot()
    else:
        print("Invalid Command")
        C3BLeave()   

def C3EBShoot():
    print("You decide to shoot back but someone throws a grenade into the room.\nYOU DIED.")
    input("Press enter to restart")
    C3EBLeave()

def C3EBCover():
    print("You run to cover and shoot someone.\nThe other person punches you and points a gun at you.\nYou hear a loud bang.\n\nYou turn around and Emma shot them.\nYou thank Emma and you prepare to leave.\n\nOptions:\nLeave basement")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE BASEMENT":
        C3EOutside()
    else:
        print("Invalid Command")
        C3EBCover() 

def C3EOutside():
    print("You both walk outside.\nYou feel cold, it seems like it could snow later.\n\nYou suddenly notice a huge crator in the distance.\nYou can drive there or walk.\n\nOptions:\nDrive\nWalk")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "DRIVE":
        C3EDrive()
    elif Select == "WALK":
        C3EWalk()
    else:
        print("Invalid Command")
        C3EOutside()     

def C3EDrive():
    print("You look at the car and the tires have been shot.\nThey must have destroyed them before they attacked.\nUnfortunetly there are no more cars near by so you will have to walk.\n\nOptions:\nWalk")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WALK":
        C3EWalk()
    else:
        print("Invalid Command")
        C3EDrive()   

def C3EWalk():
    print("You begin walking and eventually you reach the city.\nYou see lots of deserted houses.\nThey must have evacuated here.\nYou can still see the crator as you gradually get closer to it.\nYou eventually get to a bridge and there are some people nearby.\nThey seem quite friendly.\n\nOptions:\nTalk\nIgnore")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "TALK":
        C3ETalk()
    elif Select == "IGNORE":
        C3EIgnore()
    else:
        print("Invalid Command")
        C3EDrive()   

def C3EIgnore():
    print("You walk past the group\nAs you walk past you wonder if Richard is ok.\n\n\Options:\nKeep walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP WALKING":
        C3EKeepWalking()
    else:
        print("Invalid Command")
        C3EIgnore()   

def C3ETalk():
    print("You talk to them and someone said they lost some car keys for his sports car.\nYou have not seen any keys however.\nYou decide to keep walking.\n\nOptions:\nKeep walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP WALKING":
        C3EKeepWalking()
    else:
        print("Invalid Command")
        C3ETalk() 


def C3EKeepWalking():
    print("You keep walking.\nThere are a couple of holes in the wall.\nThere are also lots of signs that are littered on the road;\nMost just mention stuff about doomsday.\nJust reading that sends a chill down your spine...\n\nOptions:\nResume Walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "RESUME WALKING":
      C3EWalk2()
    else:
        print("Invalid Command")
        C3EKeepWalking()     

def C3EWalk2():
    print("You start walking again.\nYou are really close to the crater now!\n\nYou eventually reach the crater and you can see a group of people.\nWhere are they going?\n\nYou try shouting but they cannot hear you.\n\nYou should try and go to the other side of the crater to meet them at the other side.\n\nOptions:\nEnter crater")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER CRATER":
      C3RCrater()
    else:
        print("Invalid Command")
        C3EWalk2() 

def C3RCrater():
    print("You enter the crater.\nEveything within the crater has been reduced to rubble.\nIt's also very dusty.\nYou see the remains of a shelter.\n\nOptions:\nEnter shelter")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER SHELTER":
        C3ECBunker()
    else:
        print("Invalid Command")
        C3RCrater()     

def C3ECBunker():
    print("You enter the bunker.\nRubble is everywhere!\nYou can hear some voices in the distance.\nYou get closer and you can see a someone that is armed.\n\nOptions:\nSneak past\nShoot them")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SHOOT THEM":
        C3ECBShoot()
    elif Select == "SNEAK PAST":
        C3ECBSave()
    else:
        print("Invalid Command")
        C3RCrater() 

def C3ECBShoot():
    print("You shoot him.\nYou feel bad.\nEmma just looks at you.\nYou say you had to and you have to move on.\nHowever you see an exit.\n\nOptions:\nLeave bunker")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE BUNKER":
        C3ECBunkerExt()
    else:
        print("Invalid Command")
        C3ECBShoot()
        
def C3ECBSave():
    print("You sneak past but he notices you.\nYou say you just want to leave.\nHe says he is unarmed and you walk away.\n\nOptions:\nLeave bunker")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE BUNKER":
        C3ECBunkerExt()
    else:
        print("Invalid Command")
        C3ECBSave()

def C3ECBunkerExt():
    print("You leave the ruined bunker.\nHowever you start to hear thunder.\n\nYou look up.\nThe clouds are completly black and you start to see a object.\n\nIt's crashing and it looks like it's about to hit the crater!\n\nOptions:\nRun\nRun\nRun")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "RUN":
        C3ECRun()
    else:
        print("Invalid Command")
        C3ECBunkerExt()

def C3ECRun():
    print("You start running.\nYou eventually see a shelter.\nYou keep running...\n\nYou eventually get there.\nYou smash a the window and enter.\nThe walls are completly gray, there is a door that has a sign that says under renovations.\n\nOptions:\nOpen door")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "OPEN DOOR":
        C3ECSRoom()
    else:
        print("Invalid Command")
        C3ECRun()

def C3ECSRoom():
    print("You open the door and you see map on the screen.\nIt has a red dot on Lucian and one on another region.\nWhat does this mean?\nYou decide to keep looking around the room.\n\nThere is a a strange device.\n\It looks like a teleporter...\n\nOptions:\nTurn on")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "TURN ON":
        C3ECSPowerFail()
    else:
        print("Invalid Command")
        C3ECSRoom()

def C3ECSPowerFail():    
    print("You turn on the device.\nIt spins up and then shuts off.\nA screen briefly flashes power failure.\nMaybe it needs more power?\n\nEmma hands you map she found.\nThere are a couple of rooms that are intresting.\nTheres a genrator room and lots of other rooms but the names of them are redacted.\n\nOptions:\nGenerator room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GENERATOR ROOM":
        C3ECSGen()
    else:
        print("Invalid Command")
        C3ECSPowerFail()

def C3ECSGen():
    print("You turn on the generator.\nHopefully the device will work now.\nOptions:\nTest device")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "TURN ON":
       C3EEnd()
    else:
        print("Invalid Command")
        C3ECSGen()   

def C3EEnd():
    print("You turn on the device.\nIt says the teleporter is empty.\nYou told Emma you were right.\nYou step into the teleport and it starts to count down.\nThe timer reaches 0.\n\nEND OF CHAPTER.")
    input("Error 01- You have finished the game so far. press enter to restart.")
    C1intro()
    
#Starting Function
C1Start()
print("Error 00 - Misc Error")
input()
C1Intro()
#Stops program from crashing/closing due to an error or complete execution

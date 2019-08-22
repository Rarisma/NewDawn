loop = 1              #Set to anything but 1 to cause problems
Select=""             #Overwritten by player choice
#Player Variables
#Set to 1 to enable, Set to 0 to disable
Shotgun = 0           #Shotgun (Found in C2)
Keys = 1              #Keys    (Found in C2)
C3Code = 0            #Code in car (Found in C3R)

def CSMenu():
    Select = input("\nPath of a New Dawn\n\nNew game\n")
    Select=Select.upper()
    if Select == "NEW GAME":
        C1Intro()
    elif Select == "CHAPTER SELECT":
        CSChapSel()
    else:
        CSMenu()

def CSChapSel():
    Select = input("\nWelcome to Chapter Select, If a Chapter has E/R it only put one as E is the Emma variant and R is the Richard variant.\n\nChapter 2 R/E\nChapter 3 R/E\nChapter 4 R/E\nChapter 5 A\B\nChapter 6\nChapter 7\nChapter Special\n")
    Select=Select.upper()
    if Select == "CHAPTER 2 E":
        C2EStart()
    elif Select == "CHAPTER 2 R":
        C2RStart()
    elif Select == "CHAPTER 3 R":
        C3RStart()
    elif Select == "CHAPTER 3 E":
        C3EStart()
    elif Select == "CHAPTER 4 R":
        C4RStart()
    elif Select == "CHAPTER 4 E":
        C4EStart()
    elif Select == "CHAPTER 5 A":
        C5StartA()
    elif Select == "CHAPTER 5 B":
        C5StartB()
    elif Select == "CHAPTER 6":
        C6Start()
    elif Select == "CHAPTER 7":
        C7Start()
    elif Select == "CHAPTER SPECIAL":
        CSMnu()
#Essentials End
#Chapter 1 start
def C1Intro():
    Select = input("\nMy name is lucas and I live in the lucian falls apartmant building.\nMy life is pretty average but I have a great job.\nWhat was that nightmare? And why hasn't my alarm clock woke me up?\nI'm going to be late for work\n\nOptions:\nInspect plugs\nLeave bedroom\n")
    Select=Select.upper()
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
    Select = input("\nYou check the plugs.\nDid the wire break?\nI'll buy a new one after work.\n\nI have 30 minutes until I have to go to work.\n\nOptions:\nLeave bedroom\n")
    Select = Select.upper()
    if Select=="LEAVE BEDROOM":
        C1Bedroom()
    else:
        print("Invalid command")
        C1Plugs()
		
def C1Clock():
    Select = input("\nYou look at the clock, it seems 30 minutes slow.\nWhat is the current time?\nIt doesn't matter as you need to go to work\nWork starts in 30 minutes.\n\nOptions:\nLeave bedroom\n")
    Select=Select.upper()
    if Select=="LEAVE BEDROOM":
        C1Bedroom()
    else:
        print("Invalid command")
        C1Plugs()

def C1Bedroom():
    Select = input("\nI still have some time before I need to leave should I watch the TV or the Radio\n\nOptions:\nWatch TV\nListen to radio\n")
    Select=Select.upper()
    if Select=="WATCH TV":
        C1TV()
    elif Select=="LISTEN TO RADIO":
        C1Radio()
    else:
        print("Invalid command")
        C1Bedroom()

def C1Radio():
    Select = input("\nYou turn on the radio.\nYou hear somthing about a mass computer malfunction.\nThey then advise against using anything that relys on computers.\nThe audio cuts out to white noise.\n\nOptions:\nLook out the window\nLeave room\n")
    Select = Select.upper()
    if Select == "LOOK OUT THE WINDOW":
        C1Window()
    elif Select == "LEAVE ROOM":
        C1Outside()
    else:
        print("Invailid command")
        C1Radio()
        
def C1TV():
    Select = input("\nMost of the picture is blurred out, however the audio is clear.\nIt says not to use any electronics as they are malfunctioning.\nAll of a sudden the audio cuts off.\nYou wonder what to do...\n\nOptions:\nLook out the window\nLeave room\n")
    Select = Select.upper()
    if Select == "LOOK OUT THE WINDOW":
        C1Window()
    elif Select == "LEAVE ROOM":
        C1Outside()
    else:
        print("Invailid command")
        C1TV()
        
def C1Window():
    Select = input("\nYou look out of the window.\nYou see a huge riot down the street.\nYou wonder what to do about the riot.\n\nOptions:\nLeave\n")
    Select = Select.upper()
    if Select == "LEAVE":
        C1Outside()
    else:
        print("Invailid command.")
        C1Window()
        
def C1Outside():
    Select = input("\nYou leave the apartment building.\nYou can see a group of people down the road.\nYou should aproach them quietly.\n\nAproach group\n")
    Select = Select.upper()
    if Select == "APROACH GROUP":
        C1Mob()
    else:
        print("Invalid command")
        C1Outside()

def C1Mob():
    Select = input("\nYou aproach the group of people near a car.\nThey are all armed unfortunetly.\nHowever you see a gun with a suppressor.\nYou decide you should keep the suppressor on for now.\n\nOptions:\nAttack them\nHijack car\n")
    Select = Select.upper()
    if Select == "ATTACK THEM":
        C1Attack()
    elif Select == "HIJACK CAR":
        C1Hijack()
    else:
        print("Invalid command")
        C1Mob()

def C1Attack():
    Select = input("\nYou decide to attack the group.\nYou run to cover and shoot a guy in the leg.\nThe group run across the street and hide in a house.\nIt would probably be better to hijack the car.\n\nOptions:\nHijack car\nAttack the house\n")
    Select = Select.upper()
    if Select == "HIJACK CAR":
        C1Hijack()
    elif Select == "ATTACK THE HOUSE":
        print("You run towards the house and someone throws a molotov.\nYou die from third degree burns.\nYou died\npress enter to continue.")
        input("")
        C1intro()
    else:
        print("Invalid command")
        C1Attack()
        
def C1Hijack():
    Select = input("\nYou shoot towards a house to cause a distraction.\nThey run into a shop.\nYou smash the window of the car and the keys are already there.\nYou start the car and  get ready drive away.\n\nOptions:\nDrive away\nSearch car\n")
    Select = Select.upper()
    if Select == "DRIVE AWAY":
        C1Drive()
    elif Select == "SEARCH CAR":
        C1Search()
    else:
        print("Invalid command")
        C1Hijack()

def C1Search():
    Select = input("\nYou search the car and find some grenades, ammo and a crossbow bolt.\nYou throw the grenades in the shop.\nYou then get ready to drive away.\n\nOptions:\nDrive away\n")
    Select = Select.upper()
    if Select == "DRIVE AWAY":
        C1Drive()
    else:
        print("Invalid command")
        C1Search()


def C1Drive():
    Select = input("\nYou drive away.\nAs you leave Lucian Falls you wonder where to go.\nThere are 2 points listed on the satnav\n\nThe police station\nThe library\n\nYou wonder where to go...\n")
    Select = Select.upper()
    if Select == "THE POLICE STATION":
        C1Police()
    elif Select == "THE LIBRARY":
        C1Library()
    else:
        print("Invalid command")
        C1Drive()

def C1Police():
    Select = input("\nYou drive to the police station.\nIt's quite peaceful\nHowever there as some colasped buildings.\n\nOptions:\nEnter station\n")
    Select = Select.upper()
    if Select == "ENTER STATION":
        C1StationEnter()
    else:
        print("Invalid Command")
        C1Police()

def C1StationEnter():
    print("\nYou enter the police station.\nIt's barren however there is some pasta on the desk.\nIt's getting late.\nYou decide to go to sleep.\nEnd of chapter...\n\n")
    C2RStart()
    
def C1Library():
    Select = input("You drive to the library.\nMost of the buildings are untouched however some have colasped.\n\nOptions:\nEnter Library")
    Select = Select.upper()
    if Select == "ENTER LIBRARY":
        C1EnterLibrary()
    else:
        print("Invalid Command")
        C1Library()

def C1EnterLibrary():
    print("You enter the library\nIt looks abandoned.\nThere is some pizza on the desk and getting late.\nYou decide to go to sleep.\n\nEnd of chapter...\n\n")
    C2EStart()

def C2RStart():
    Select = input("\nYou wake up.\nYou can smell smoke...\nThe cafe is on fire!\n\nYou run and escape.\nHowever you loose the suppressor.\nYou run to the car and start to drive.\nYou decide to drive to a nearby town\n\nOptions:\nStart driving\n")
    Select = Select.upper()
    if Select == "START DRIVING":
        C2RTown()
    else:
        print("Invailid Command")
        C2RStart()

def C2RTown():
    Select = input("\nYou drive into the town and you see a group of people\nThey try and shoot at you...\nHowever they miss.\nYou keep driving and eventually park near 2 shops.\n\nOptions:\nEnter shop\nRob shop\nPC shop\nLeave\n")
    Select = Select.upper()
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
    Select = input("\nYou run in and shoot the shopkeeper.\nGet what you need and leave.\n\nOptions:\nLeave\n")
    Select = Select.upper()
    if Select == "LEAVE":
        C2RLeave()
    else:
        print("Invalid Command")
        C2RobStore
        
def C2RStoreChat():
    Select = input("\nYou enter the store.\nSuprisingly the owner is still inside\nYou talk for awhile and he gives you some food and water.\n\nOptions:\nLeave\n")
    Select = Select.upper()
    if Select == "LEAVE":
        C2RLeave()
    else:
        print("Invalid Command")
        C2RStoreChat()   
        
def C2RPC():
    input("You enter the PC store.\nAll of a sudden the store exploded.\nYou died...\n\nPress enter to continue\n")
    C2RTown()

def C2RLeave():
    Select = input("\nYou get in you car and get ready to leave\nYou start the car and decide to drive to, Richard's house\nAs you get into the city the fuel indicator flashes meaning that you will have to refuel soon.\nHowever you can keep driving for now.\nYou eventually reach a fork in the road.\n\nOptions:\nGo left\nGo right\n")
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
    Select = input("\nYou drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...\n\Options:\nAttack\nGo back\n")
    Select = Select.upper()
    if Select == "ATTACK":
        C2RAttack()
    elif Select == "GO BACK":
        C2RRight()
    else:
        print("Invalid Command")
        C2RLeave()
        
def C2RAttack():
    input("You run at them but you get shot before you can do anything.\n\nYou died...\n\nPres enter to restart\n")
    C2RTown()

def C2RRight():
    Select = input("\nYou start driving right.\nThis area of the city is realativly barren.\nHowever there is a building with the words dual take\nBut it seems beyond repair...\nUnexpectedly your car starts slowing down and eventually stops\n\nOptions:\nInspect car\n")
    Select = Select.upper()
    if Select == "INSPECT CAR":
        C2RCar()
    else:
        print("Invalid Command")
        C2RRight()

def C2RCar():
    Select = input("\nYou check the car and it's definitely out of petrol.\nThere are some buildings nearby.\nYou should check nearby.\n\nOptions\nCheck house\nCheck shop\n")
    Select = Select.upper()
    if Select == "CHECK HOUSE":
        C2RHouse()
    elif Select == "CHECK SHOP":
        C2RShop()
    else:
        print("Invalid Command")
        C2RCar()
        
def C2RHouse():
    Select = input("\nYou check the house.\nThere are some keys on the shelf.\nDespite there being no cars other than yours nearby.\nYou got the Strange keys.\nHowever there is no petrol in sight.\n\nOptions:\nCheck shop\n")
    Select = Select.upper()
    if Select == "CHECK SHOP":
        C2RShop()
    else:
        print("Invalid Command")
        C2RHouse()

def C2RShop():
    Select = input("\nYou enter the shop.\nIt looks like it has been abandoned for awhile.\nHowever there are still cans of petrol and other items on the self.\nYou go back and refill the car.\n\nOptions:\nStart driving\n")
    Select = Select.upper()
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
    Select = input("\nYou drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...\n\nOptions:\nAttack\nGo back\n")
    Select = Select.upper()
    if Select == "ATTACK":
        C2RAttack()
    else:
        print("Invalid Command.")

def C2RRam():
    input("\nYour car has run out of fuel.\nYou try restarting the car but you are quickly noticed.\nYou get shot\nYou died.\nPress enter to restart\n")
    C2RShop()

def C2RShotgun():
    Select = input("\nYou sneak up and shoot them with shotgun.\nYou break the barricade and you can keep driving.\n\nOptions\nKeep driving\n")
    Select = Select.upper()
    if Select == "KEEP DRIVING":
        C2RKeepDriving()
    else:
        print("Invalid Command")
        C2RShotgun()
        
def C2RSneak():
    Select = input("\nYou sneak around them but you have to ditch the car and everything in it.\nYou will need to find another car...\n\nOptions:\nLook around\n")
    Select = Select.upper()
    if Select == "LOOK AROUND":
        C2RFindCar()
    else:
        print("Invalid Command")
        C2RSneak()

def C2RFindCar():
    Select = input("\nYou look arround and you see a car thats abandoned.\nYou jump and start the car.\nou can now continue driving.\n\nOptions:\nKeep driving\n")
    Select = Select.upper()
    if Select == "KEEP DRIVING":
        C2RKeepDriving()
    else:
        print("Invalid Command")
        C2RFindCar()

def C2RKeepDriving():
    Select = input("\nYou keep driving.\nYou are almost at Richards's appartment.\nAs you get closer you see signs that are displaying a countdown.\nYou wonder what they mean.\n\nOptions:\nDrive\n")
    Select = Select.upper()
    if Select == "DRIVE":
        C2REND()
    else:
        print("Invalid Command")
        C2RKeepDriving()

def C2REND():
    print("\nYou knock on the door and the timers reach 0.\nShe says the countdown is about to reach 0\nYou ask about what she means.\nShe says it has been hacked and is about to launch.\nYou hear a rocket launch.\nYou run back to your car and start driving.\nAfter arriving someone pulls you inside of a building.\nEnd of chapter...\n")
    C3RStart()
#Chapter 2R End
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
    Select = input("\nYou drive into the town and you see a group of people\nThey try and shoot at you...\nHowever they miss.\nYou keep driving and eventually park near 2 shops.\n\nOptions:\nEnter shop\nRob shop\nPC shop\nLeave\n")
    Select = Select.upper()
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
    Select = input("\nYou run in and point the pistol at the shop keeper however he shoots you.\nYou died press enter to restart\n")
    C2ETown()

        
def C2EStoreChat():
    Select = input("\nYou enter the store.\nSuprisingly the owner is still inside\nYou talk for awhile and he gives you some food and water.\n\nOptions:\nLeave\n")
    Select = Select.upper()
    if Select == "LEAVE":
        C2ELeave()
    else:
        print("Invalid Command")
        C2EStoreChat()   
        
def C2EPC():
    input("\nYou enter the PC store.\nAll of a sudden the store exploded.\nYou died...\nPress enter to continue\n")
    C2ETown()

def C2ELeave():
    Select = input("\nYou get in you car and get ready to leave\nYou start the car and decide to drive to Emma's house\nAs you get into the city the fuel indicator flashes meaning\nthat you will have to refuel soon.\nHowever you can keep driving for now.\nYou eventually reach a fork in the road.\nOptions:\nGo left\nGo right\n")
    Select = Select.upper()
    if Select == "GO RIGHT":
        C2ERight()
    elif Select == "GO LEFT":
        C2ELeft()
    else:
        print("Invalid Command")
        C2ELeave()
    
def C2ELeft():
    Select = input("\nYou drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...\n\Options:\nAttack\nGo back\n")
    Select = Select.upper()
    if Select == "ATTACK":
        C2EAttack()
    elif Select == "GO BACK":
        C2ERight()

def C2EAttack():
    input("\nYou run at them but you get shot before you can do anything.\nYou died...\nPres enter to restart\n")
    C2ETown()

def C2ERight():
    Select = input("\nYou start driving right.\nThis area of the city is realativly barren.\nHowever there is a building with the words dual take\nBut it seems beyond repair...\nUnexpectedly your car starts slowing down and eventually stops\n\nOptions:\nInspect car\n")#ちょっとなぜあなたはデュアルテイクケーキを放棄しましたか？
    Select = Select.upper()
    if Select == "INSPECT CAR":
        C2ECar()
    else:
        print("Invalid Command")
        C2ERight()

def C2ECar():
    Select = input("\nYou check the car and it's definitely out of petrol.\nThere are some buildings nearby.\nYou should check nearby.\n\nOptions\nCheck house\nCheck shop\n")
    Select = Select.upper()
    if Select == "CHECK HOUSE":
        C2EHouse()
    elif Select == "CHECK SHOP":
        C2EShop()
    else:
        print("Invalid Command")
        C2ECar()
        
def C2EHouse():
    Select = input("\nYou check the house.\nThere are some keys on the shelf.\nDespite there being no cars other than yours nearby.\nYou got the Strange keys.\nHowever there is no petrol in sight.\n\nOptions:\nCheck shop\n")
    Select = Select.upper()
    if Select == "CHECK SHOP":
        C2EShop()
    else:
        print("Invalid Command")
        C2EHouse()

def C2EShop():
    Select = input("\nYou enter the shop.\nIt looks like it has been abandoned for awhile.\nHowever there are still cans of petrol and other items on the self.\nYou go back and refill the car.\n\nOptions:\nStart driving\n")
    Select = Select.upper()
    if Select == "START DRIVING":
        C2ECar()
    else:
        print("Invalid Command")
        C2EShop()

def C2ECar():
    print("\nYou see another group that have blocked the road.\nIt seems like they are waiting to hijack a car.\nWhat should you do?\n\nOptions:\nSneak through\nDrive through")
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
    Select = input("\nYou drive left and you see a group of crimals.\nThey have put up a kind of make-shift barricade.\nHowever with the suppressor you chances arent likely...\n\nOptions:\nAttack\nGo back\n")
    Select = Select.upper()
    if Select == "ATTACK":
        C2EAttack()
    else:
        print("Invalid Command")
        C2ECar()        

def C2ERam():
    input("\nThe car has ran out of fuel\nHowever trying to start it has attracted their attention.\nYou died.\nPress enter to restart\n")
    C2ELeft()

def C2EShotgun():
    Select = input("\nYou sneak up and shoot them with shotgun.\nYou break the barricade and you can keep driving.\n\nOptions\nKeep driving\n")
    Select = Select.upper()
    if Select == "KEEP DRIVING":
        C2EKeepDriving()
    else:
        print("Invalid Command")
        C2EShotgun()
        
def C2ESneak():
    Select = input("\nYou sneak arround them but you have to ditch the car and everything in it.\nYou will need to find another car...\n\nOptions:\nLook around\n")
    Select = Select.upper()
    if Select == "LOOK AROUND":
        C2EFindCar()
    else:
        print("Invalid Command")
        C2ESneak()

def C2EFindCar():
    Select = input("\nYou look arround and you see a car thats abandoned.\nYou get in and start the car.\nou can now continue driving.\n\nOptions:\nKeep driving\n")
    Select = Select.upper()
    if Select == "KEEP DRIVING":
        C2EKeepDriving()
    else:
        print("Invalid Command")
        C2EFindCar()

def C2EKeepDriving():
    Select = input("\nYou keep driving.\nYou are almost at Emmas's appartment.\nAs you get closer you see signs that are displaying a countdown.\nYou wonder what they mean.\n\nOptions:\nDrive\n")
    Select = Select.upper()
    if Select == "DRIVE":
        C2EEND()
    else:
        print("Invalid Command")
        C2EKeepDriving()

def C2EEND():
    print("\nYou knock on the door and the timers reach 0.\nShe says the countdown is about to reach 0.\nYou ask about what she means.\nShe says an experemental rocket has been hacked and is about to launch\nYou hear a rocket launch.\nEnd of chapter...\n")
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
    C4RStart()
#C3R End
#C3E Start
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
    print("After awhile you both get bored of talking and Emma brings out two boxes.\nThey are both board games.\nOne box reads Hippos and the other is Checkers.\n\nWhich game should you play?\nHippo\nCheckers")
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
    print("You decide to play checkers.\nYou are very skilled.\nYou put the hippo game back while Emma opens the box and reads the rules.\n\nYou played a couple of matches and you won every match except one.\nYou are the checkers master...\n\nQuite a bit of time has passed.\nMaybe you can go outside now?\n\nOptions:\nPlay again\nGo outside")
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
    print("You decide to shoot back but someone shoots you first.\nYOU DIED.")
    input("Press enter to restart")
    C3BLeave()

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
    print("You open the door and you see map on the screen.\nIt has a red dot on Lucian and one on another region.\nWhat does this mean?\nYou decide to keep looking around the room.\n\nThere is a a strange device.\n\nIt looks like a teleporter...\n\nOptions:\nTurn on")
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
    if Select == "TEST DEVICE":
       C3EEnd()
    else:
        print("Invalid Command")
        C3ECSGen()   

def C3EEnd():
    print("You turn on the device.\nIt says the teleporter is empty.\nYou told Emma you were right.\nYou step into the teleporter and it starts to count down.\nThe timer reaches 0.\n\nEND OF CHAPTER.")
    C4EStart()
#C3E End
#C4R Start

def C4RStart():
    print("You enter the cells.\nThere are a couple of cells but you can hear someone shouting.\nThere are 3 cells.\nYou wonder what cell you should look at 1st.\n\nCell 1\nCell 2\nCell 3")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CELL 1":
        C4RPC1()
    elif Select == "CELL 2":
        C4RPC2()
    elif Select == "CELL 3":
        C4RPC3()
    else:
        print("Invalid Command")
        C4RStart() 

def C4RPC1():
    print("The cell has completly colasped.\nThere are some shreds of a poster but it's unreadable.\nThere is also a sign that mentions entering parliment in armour is a crime?\n\nOptions:\nCell block")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CELL BLOCK":
        C4RStart()
    else:
        print("Invalid Command")
        C4RPC1()

def C4RPC2():
    print("You look at the cell.\nThe wall is filled with mathmatical ratios.\nOne wall is even dedicated to the numbers of pi.\n\nOptions:\nCell block")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CELL BLOCK":
        C4RStart()
    else:
        print("Invalid Command")
        C4RPC2()

def C4RPC3():
    print("You look at the Cell 3.\nRichard asks you to open the door.\nYou shoot the lock and open the gate.\nRichard explains that the door locked automaticly for some reason.\nYou decide to tell him about the shelter collasping.\nHe says that we need to get out of here.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C4RPCLeave()
    else:
        print("Invalid Command")
        C4RPC3()    

def C4RPCLeave():
    print("You both leave and Richard he tells you that there is a bunker nearby.\n\nAs you leave the prison Richard asks you about about the rocket.\nYou tell him that it launched.\n\nHe tells you that it released EMP designed for testing inventions.\n\nHowever he doesn't know much else.\nYou both eventually leave.\n\nOptions:\nLeave prison")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE PRISON":
        C4RBEnterance()
    else:
        print("Invalid Command")
        C4RPCLeave()     

def C4RBEnterance():
    print("You leave the prison and run to the bunker.\nSuprisingly it's not that far away.\n\nYou smash a window and get in.\n\nRichard looks shocked.\nYou ask him whats wrong,\nHe says that it's completly empty!\nYou decide to look around the bunker.\n\nOption:\nExplore")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "EXPLORE":
        C4RBTeleport()
    else:
        print("Invalid Command")
        C4RBEnterance()

def C4RBTeleport():
    print("You look around some of the rooms but they are all empty.\nHowever Richard finds a elevator and he manages to force it open.\n\nOptions:\nEnter elevator")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER ELEVATOR":
        C4RBElevator()
    else:
        print("Invalid Command")
        C4RBTeleport()

def C4RBElevator():
    print("You enter the lift.\nMost of the buttons aren't lit.\nRichard presses a button and the elevator starts moving.\n\nAfter awhile the elevator doors open.\nOptions:\nLeave elevator")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ELEVATOR":
        C4RBCoridor()
    else:
        print("Invalid Command")
        C4RBElevator()

def C4RBCoridor():
    print("You leave the elevator.\nRichard walks towards a door and he says there is a party.\nHe tell you that you should go backstage.\n\nYou enter the room.\nThe room is huge and there are lots of people dancing.\nBoth of you go backstage.\nRichard tells you to cut the power.\n\nOptions:\nShoot sandbag\nCut power")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CUT POWER":
        C4RBBP()
    elif Select == "SHOOT SANDBAG":
        C4RBBS()
    else:
        print("Invalid Command")
        C4RBCoridor()
    
def C4RBBP():
    print("You cut the power and run through the backdoor.\nPeople start to scream!\n\nOptions:\nLeave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C4RBBackstage()
    else:
        print("Invalid Command")
        C4RBBP()

def C4RBBS():
    print("You shoot the sandbag and it hits someone.\nYou run through the backdoor.\n\nOptions:\nLeave Room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C4RBBackstage()
    else:
        print("Invalid Command")
        C4RBBS()        

def C4RBBackstage():
    print("You walk past and Richard grabs a keycard.\nAfter you leave you ask Richard what he got.\nHe says that he got a keycard but he needs a higher ranking one.\nYou ask Richard where you find one.\nHe tells you that the IT room is down the hall.\n\nOptions:\nIT Room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "IT ROOM":
        C4RBITRoom()
    else:
        print("Invalid Command")
        C4RBBackstage()

def C4RBITRoom():
    print("You enter the IT room and the walls are filled with servers.\nThere is a room thats filled people that could help you to get a higher level keycard.\nYou ask Richard what you should do.\nHe hands you the keycard and he tells you to ask for a higher level card.\n\nOptions:\nOpen door")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "OPEN DOOR":
        C4RBITKey()
    else:
        print("Invalid Command")
        C4RBITRoom()    

def C4RBITKey():
    print("You enter the room and say you are from support.\nThey sigh and say it took you long enough.\nA man aproaches you and asks you what you need.\nYou tell him that you are doing maintainance on the power box and other computers but you need a higher level keycard.\nHe looks annoyed and justs gives you his keycard.\n\nOptions:\nLeave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C4RBITKey1()
    else:
        print("Invalid Command")
        C4RBITKey()

def C4RBITKey1():
    print("You walk out and tell Richard that it was easy.\nHe looks suprised but tells you that you need to leave.\nRichard says he has a grenade and he throws it into the server room.\nYou both run out.\n\nRichard tells you that you need to get to the lift.\n\nOptions:\nGo to lift")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO TO LIFT":
        C4REnd()
    else:
        print("Invalid Command")
        C4RBITKey1()

def C4REnd():
    print("You run to the elevator and scan the keycard.\nAll of the buttons light up.\nRichard presses a low button.\nThe door opens and you see Emma?\n\nEND OF CHAPTER")
    C5StartA()
#C4R End
#C4E Start

def C4EStart():
    print("You wake up.\nYou cannot feel anything and you can see lots of bright lights.\nSomeone walks towards you and holds out their hand.\n\nYou grab their hand and after awhile your vision clears up.\nYou see Emma.\nYou tell her that you never want to teleport again.\n\nOptions:\nLook around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C4EBLook()
    else:
        print("Invalid Command")
        C4EStart()

def C4EBLook():
    print("You look around and the walls are painted a dull white.\nFurthermore there are a couple of computers scattered around room and there is a hologram on the door.\nYou should check out the door.\n\nOptions:\nCheck computer\nCheck door")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK DOOR":
        C4EBDoor()
    elif Select == "CHECK COMPUTER":
        C4EBComputer()
    else:
        print("Invalid Command")
        C4EBLook()    

def C4EBComputer():
    print("You check the computer.\nIt's full of text that seems to be in latin.\nUnfortunetly you cannot read latin\nYou should probably check the door.\n\nOptions:\nCheck door")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK DOOR":
        C4EBDoor()
    else:
        print("Invalid Command")
        C4EBComputer()    

def C4EBDoor():
    print("You look at the door pannel.\nIt looks very complicated but you can see a button labeled open door.\n\nYou open the door however Emma is still looking at the door pannel.\nShe manages to turn off the lights and she finds a somthing about the rocket.\nEmma tells you to read it.\n\nIt reads:\nThe Rocket project has been in development for several years.\nWe eventually decided that we wish to change the world\nWe have recuited new members that will patrol the streets.\nWe have the more skilled members ready in key positions.\nHowever the file ends there.\n\nOptions:\nLeave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C4EBCorridor()
    else:
        print("Invalid Command")
        C4EBDoor()        

def C4EBCorridor():
    print("You walk into the corridor carefully and the lights flicker on.\nThe walls are a glossy shade of red.\nThere are also some pictures of test rockets.\n\nAfter awhile of walking down the hallway you see a portait of workers.\nBizzarly Richards face has been crossed out.\n\nYou need to find Richard.\n\nYou eventually see that you can go left or right.\n\nOptions:\nGo left\nGo right")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO RIGHT":
        C4EBRight()
    elif Select == "GO LEFT":
        C4EBLeft()
    else:
        print("Invalid Command")
        C4EBCorridor() 

def C4EBLeft():
    print("You go left.\nHowever you see many people surround a hall.\nThey start going into the conference hall but some security stay outside.\nIt's probably better if you went right instead.\n\nOptions:\nGo right")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO RIGHT":
        C4EBRight()
    else:
        print("Invalid Command")
        C4EBLeft() 

def C4EBRight():
    print("You walk right and enter a huge conference hall.\nSome people are holding a huge party!\nYou walk towards a outfit and tell Emma to put it on and blend in.\nYou tell Emma to grab that keycard when the power goes out.\n\nEmma walks toward the DJ and starts a coverseration.\nTime to cut the power...\n\nOptions:\nCut power")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CUT POWER":
        C4EBPwr()
    else:
        print("Invalid Command")
        C4EBRight()

def C4EBPwr():
    print("You cut the power.\nPeople start screaming and Emma runs towards the exit.\nA couple of minutes later the power turn back on\n\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C4EBElevator()
    else:
        print("Invalid Command")
        C4EBPwr()    

def C4EBElevator():
    print("You run to the exit and Emma scans the key key card.\nSome of the buttons light up and Emma presses the B3 button\nThe elevator slowly moves and then suddenly stops.\n\nThe door opens slightly and you hear Richard shout at you.\nYou tell Richard that it's you.\nHe calms down and tells you that you need a higher level keycard to get down here.\n\nHe hands you a guide and tells you to go to B2\n\nEmma presses B2 while you read the manual.\nYou eventually find that you can speed up and slow down.\n\nYou hold the speed++ button and you reach B2 at high speeds!\n\nOptions:\nB2")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "B2":
        C4EB2()
    else:
        print("Invalid Command")
        C4EBElevator()

def C4EB2():
    print("You arrive at floor B2.\nMost of the rooms look empty except for the lunch room.\nEmma says you should check the Alchemist room.\n\nOptions:\nAlchemist room\nLunch room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ALCHEMIST ROOM":
        C4EB2Alchemist()
    elif Select == "LUNCH ROOM":
        C4ELunch()
    else:
        print("Invalid Command")
        C4EB2()

def C4ELunch():
    print("You enter the lunch room and somebody shoots you.\nGAME OVER\nPress enter to restart")
    Select = input()
    C4ELunch()

def C4EB2Alchemist():
    print("You enter the Alchemist room.\nIt's very dark but Emma finds the light switch.\n\nThe entire room lights up with bright floodlights\n\nIn the back of the room there is a computer.\nAfter awhile of reading you find out that the rocket will cause a horrible winter and is just a diversion.\n\nWhile you were reading Emma found some smoke grenades.\nYou should check the Engineering room.\n\nOptions:\nEngineering room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENGINEERING ROOM":
        C4B2Engineer()
    else:
        print("Invalid Command")
        C4EB2Alchemist()

def C4B2Engineer():
    print("You enter the engineering room.\nIt's quite empty however theres a car and some soldiering tools.\n\nA bell rings and you both hide behind a table.\nMultiple people storm the room and tell you to put your hands up\n\nOptions:\nThrow grenades\nSurrender")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SURRENDER":
        C4Surrender()
    elif Select == "THROW GRENADES":
        C4Fighton()
    else:
        print("Invalid Command")
        C4B2Engineer()    

def C4Surrender():
    print("You put your hand up and you are arrested.\nEmma trys to escape but is also arrested.\n\nEND OF CHAPTER")
    C5StartB()

def C4Fighton():
    print("Emma hands you a smoke grenade and a molotov cocktail.\nYou put your hands up to surrender but you roll the smoke grenade.\n\nThe grenade explodes and you and emma jump over the table.\nYou turn arround and light and throw the molotov.\n\nAfter waiting for the flames to die out you grab a key card and run to the elevator.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C4EEND()
    else:
        print("Invalid Command")
        C4Fighton()    

def C4EEND():
    print("You run to the elevator and slam B2.\nThe lights suddenly turn off and the doors open.\n\nEND OF CHAPTER.")
    C5StartA()
    
def C5StartA():
    print("The doors open and you are surrounded by guards.\n\nEmma hits another button and the elevator shoots up to B1.\nThe doors open and the floor is empty.\nRichard taps you on the shoulder and tells you to follow him.\n\nOptions:\nFollow Richard")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "FOLLOW RICHARD":
        C5Follow()
    else:
        print("Invalid Command")
        C5StartA()
        
def C5StartB():
    print("You are taken to the elevator.\nAs the the doors open Emma throws a grenade and runs.\nYou run and you eventually manage to find the stairs.\n\nYou reach B2 but the you notice the elevator is surrounded so you run to B1.\n\nAfter some more running you eventually reach B1 and after looking around for awhile Richard taps you on the shoulder.\nHe gives you a gun and he tells you not to lose it this time.\nHe then tells you to follow him.\n\nFollow Richard")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "FOLLOW RICHARD":
        C5Follow()
    else:
        print("Invalid Command")
        C5StartB() 

def C5Follow():
    print("You follow Richard and he leads you to a large room.\nHe tells you that it's crucial to get some answers from the Vice President.\n\nYou tell him that you are ready.\n\nOptions:\nEnter")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER":
        C5Conference()
    else:
        print("Invalid Command")
        C5Follow()     

def C5Conference():
    print("Richard counts down from 5.\nYou run in and point a gun at the VP.\nSome guards run at you but Richard shoots a warning shot and they stop.\n\nYou tell everyone to leave the room.\nMost people comply but some stand still.\nYou decide to shout at them to get down.\n\nRichard walks towards the VP and starts to question him.\n\nAfter awhile Richard tells Emma to pull the fire alarm.\nRichard tells everyone to go.\n\nOptions:\nEscape")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ESCAPE":
        C5Escape()
    else:
        print("Invalid Command")
        C5Conference() 

def C5Escape():
    print("You ask Richard how to escape.\nRichard says the enterance is above you.\nHe runs up the stairs.\nHe runs back and he says it's blocked.\n\nEmma says there is a car downstairs.\n\nOptions:\nGo downstairs")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO DOWNSTAIRS":
        C5Downstairs()
    else:
        print("Invalid Command")
        C5Escape() 

def C5Downstairs():
    print("You run downstairs and all of the doors have been disarmed but the elevators are disabled.\n\nEmma gets in the car and it starts automatically.\nRichard tells you it's a self driving car prototype.\n\nHe looks at a tablet and puts in a location of a village.\n\nThe car starts driving and it exits the garage.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C5Outside()
    else:
        print("Invalid Command")
        C5Downstairs()

def C5Outside():
    print("The car leaves the bunker.\nYou immedietly feel the cold wind.\n\nRichard starts explaining that the rocket is just the start of the plan.\nRichard then reveals that he used to work on the rocket but he abandoned it about 2 weeks ago.\nHe tells you that there is a kill switch but he needs time to get it ready.\n\nHe explains that the company is trying to colonise mars but decide against it for some reason.\n\nThe car announces that manual drive has been disabled.\nIt then announces that the car has a critcial system failure.\n\nEmma stops the car and you decide to walk to a nearby village\n\nOptions:\nStart walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START WALKING":
        C5Walk()
    else:
        print("Invalid Command")
        C5Outside()


def C5Walk():
    print("You start walking towards a village.\nEmma starts questioning Richard about his job.\nIt turns out that he is a aerospace engineer.\nHe got fired for probing the rocket and it causing an earthquake.\nHe says its programmed to disrupt the country.\nHe doesn't know why though.\n\nYou eventually reach the village.\n\nOptions:\nLook around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C5Village()
    else:
        print("Invalid Command")
        C5Walk()

def C5Village():
    print("You look around the village.\nIt's empty, nobody is in sight.\nMost of the doors have been covered with snow.\n\nYou all decide that you should get to shelter quickly.\nAfter looking around you see several buildings.\n\nOptions:\nVillage Hall\nOffice\nGarage\nPC Shop")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "VILLAGE HALL":
        C5Shelter()
    elif Select == "OFFICE":
        C5Shelter()
    elif Select == "GARAGE":
        C5Shelter()
    elif Select == "PC SHOP":
        C5PCShop()
    else:
        print("Invalid Command")
        C5Village() 

def C5Shelter():
    print("You run inside.\nYou quickly realise it's getting late.\nRichard finds some sleeping bags and Emma looks around for some food.\n\nYou decide to look at a map.\nRichard has already circled a abandoned building,\nYou decide to leave the map alone.\n\nOptions:\nAsk questions\nSleep")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ASK QUESTIONS":
        C5SQuestions()
    elif Select == "SLEEP":
        C5Sleep()
    else:
        print("Invalid Command")
        C5Shelter()

def C5PCShop():
    print("You walk upto the PC Shop and Richard tells you to leave as it will kill you.\nEmma has found an empty office anyway.\n\nHowever the door is snowed in.\n\nYou freeze to death.\n\nGame over?") #Until you defrost.
    input("Press enter to go back.")
    C5Walk()

def C5SQuestions():
    print("You decide to ask Emma how she is.\nEmma says she is tierd.\n\nYou ask Richard the same question.\nHe says he is exhausted.\n\nYou decide to go to bed.")
    C5Sleep()

def C5Sleep():
    print("Emma puts 2 bowls of soup on the table.\nYou drink the soup while watching the rampant blizard.\nAfter that you lay down and go to sleep.\n\nOptions:\nWake up")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WAKE UP":
        C5Wake()
    else:
        print("Invalid command.")
        C5Sleep()

def C5Wake():
    print("You wake up and you notice Emma and Richard are missing.\nYou look around and you eventually find them both downstairs.\n\nYou quickly realise you have been snowed in.\n\nOptions:\nShovel snow")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SHOVEL SNOW":
        C5Snow()
    else:
        print("Invalid command.")
        C5Wake()
    
def C5Snow():
    print("Emma hands a shovel and you all start to shovel snow.\nA few hours pass but you eventually leave the office.\nRichard tells you that there is an abandoned lab about a Killometer from here.\n\nOptions:\nStart Walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "START WALKING":
        C5SnowWalk()
    else:
        print("Invalid command.")
        C5Snow()    

def C5SnowWalk():
    print("You start walking however the blizard seems to be clearing up.\nThe old lab is in sight and Richard starts explaining the lab is actually a old computer lab.\n\nYou eventually get there.\n\nEnter computer lab")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER COMPUTER LAB":
        C5END()
    else:
        print("Invalid command.")
        C5SnowWalk()        

def C5END():
    print("You enter the computer lab and all of the screens suddenly light up.\nThey just unlock, with no password it seems they have been recently used but the lab is empty.\n\nEmma finds a car but the battery is dead.\n\nRichard plugs the battery in and it starts to charge.\nThe battery will take 5/6 hours to charge.\nYou decide to lay down for awhile.\n\nEND OF CHAPTER.")
    C6Start()

def C6Start():
    print("Richard wakes you and he tells you that the car is ready.\nThe garage door slowly opens but you hear a loud crash.\nIt seems someone is here.\n\nYou stop the car and get out and you see the lab is being raided, but by who?,\nRichard grabs Emma and jumps into the car.\nYou frantically run to the car.\n\nOptions:\nShoot back\nDrive faster")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SHOOT BACK":
        C6Shoot()
    elif Select == "DRIVE FASTER":
        print("")
        C6Drive213()
    else:
        print("Invalid command.")
        C6Start()

def C6Shoot():
    print("You shoot back and you seem to ignite some petrol.\nThe lab is set on fire but it seems to be quickly extinguished.\n\nOptions:\nKeep driving")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP DRIVING":
        C6Drive()
    else:
        print("Invalid command.")
        C6Shoot()
    
def C6Drive213():   #these numbers mean nothing but python wasn't working correctly this fixed the linking
    print("You start driving and push the pedal to go faster.\nHowever some motorbikes start following you.\nYou start shooting at the bikes however Richard starts franticly typing into the cars console and the car starts speeding up.\nEmma passes you a grenade launcher.\n\nIt's quite small and you start shooting.\nYou shoot and most of the bikes explode.\nHowever the car starts to slow down and some one shoots the tire with a machine gun.\nYou decide to jump from the car.\n\nOptions:\nLook around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C6City()
    else:
        print("Invalid command.")
        C6Drive()

def C6City():
    print("\nYou panic and jump out the car.\n\nOptions:\nLook Around")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK AROUND":
        C6Look()
    else:
        print("Invalid command.")
        C6City()

def C6Look():
    print("You look around and you see a house.\nYou run towards the house.\nAfter awhile you see the motorbikes speed past.\n\nYou wonder what happened to Emma and Richard.\n\nOptions:\nWait")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WAIT":
        C6Time()
    else:
        print("Invalid command.")
        C6Look()

def C6Time():   #TIME       GENTLEMEN       PLEASE.
    print("You wait awhile and it seems nobody else is coming.\n\nYou see a huge building in the distance.\nThis must be the CEO's buildings.\nThey are probably at the top floor.\n\nHowever you need a car to get there.\n\nOptions:\nLook for a car")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK FOR A CAR":
        C6Street()
    else:
        print("Invalid command.")
        C6Time()    

def C6Street():
    print("You walk down the street.\nThey are completly empty, what happened here?\n\nYou wonder why you have saw almost nobody.\nYou find multiple cars in a abandoned garage.\nYou pick a small motobike.\nAfter grabbing the keys you drive towards the building.\n\nOptions:\nDrive")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "DRIVE":
        C6Drive()
    else:
        print("Invalid command.")
        C6Street()    

def C6Drive():
    print("You start driving towards the building.\nYou notice how the roads are completly barren.\nYou eventually arrive at the city.\nHowever you see someone guarding the enterance.\nThe security seems supprisingly lax.\n\nOptions:\nShoot him")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SHOOT HIM":
        C6CEOATK()
    else:
        print("Invalid command.")
        C6Drive()        

def C6CEOATK():
    print("You drive towards him and shoot him.\nAfter getting off the bike you find that all the doors have been boarded up.\nYou get a pistol from the guy but they don't have a key.\nYou should look for another enterance.\n\nOptions:\nLook for an enterance")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK FOR AN ENTERANCE":
        C6Enterance()
    else:
        print("Invalid command.")
        C6CEOATK()        

def C6Enterance():
    print("You look for an enterance and you see some people are breaking into a house.\nMaybe they will have somthing to help you to break into the building.\n\nOptions:\nAproach")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "APROACH":
        C6Fight()
    else:
        print("Invalid command.")
        C6Enterance()        

def C6Fight():
    print("You decide you can either shoot them or blow up the motorbike\n\nOptions:\nMotorbike\nShoot them")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "MOTORBIKE":
        C6MotoFight()   
    elif Select == "SHOOT THEM":
        C6Jonothan()
    else:
        print("Invalid command.")
        C6Fight()

def C6MotoFight():
    print("You start driving towards them and you jump from the bike.\nThe bike explodes and the house is englufed in fire.\nAfter the fire dies down you find a axe!.\n\nOptions:\nBreak in")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "BREAK IN":
        C6BreakIn()
    else:
        print("Invalid command.")
        C6MotoFight()        

def C6Jonothan():
    print("You walk towards them and you start shooting them.\bUnfortunetly you realise that you are outgunned.\nThey thow a grenade at you but they miss.\nYou quickly leave.\n\nAfter waiting a for awhile you realise that the group seems to have left.\nYou eventually find a axe.\n\nOptions:\nBreak in")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "BREAK IN":
        C6BreakIn()
    else:
        print("Invalid command.")
        C6Jonothan()
        
def C6BreakIn():
    print("You break in to the building with the axe.\n\nThe floor is entirely barren but there is a elevator.\nYou enter the elevator\n\nOptions:\nFloor A\nFloor B\nStorage floor")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "FLOOR A":
        C6FA()
    elif Select == "FLOOR B":
        C6FB()
    elif Select == "STORAGE FLOOR":
        C6Storage()
    else:
        print("Invalid command.")
        C6BreakIn()

def C6FA():
    print("You decide to go to floor A.\nIt seems that this floor is full of old documents.\nYou decide to read a few.\n\nLucian Falls floor plans:\nIt describes Lucian Falls in great detail however it seems that the current lucian falls is not finished.\n\nThe other documents are about cyber secuity, Phone number and law documents.\n\nYou should see what's in the storage room\n\nOptions:\nFloor B\nStorage floor")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "FLOOR B":
        C6FB()
    elif Select == "STORAGE FLOOR":
        C6Storage()
    else:
        print("Invalid command.")
        C6FA()

def C6FB():
    print("You go to floor B.\nThe floor seems to be full of money laundering equiment.\nYou decide to damage some of it.\nYou should go to floor A\n\nOptions:\nFloor A\nStorage floor")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "FLOOR A":
        C6FA()
    elif Select == "STORAGE FLOOR":
        C6Storage()
    else:
        print("Invalid command.")
        C6FB()

def C6Storage():
    print("You go to storage floor.\nYou reload your pistol and you realise you are on your last clip.\n\nThe doors open and you are quickly spotted.\nSomeone reaches for a radio but you quickly shoot them\nThe radio heard the gunshot.\nEveryone knows you are here.\nAt the other end of the room you see a large cargo elevator.\nYou run to the elevator but you are quickly surrounded\n\nEND OF CHAPTER")
    C7Start()

def C7Start():
    print("You dive behind some boxes.\nYou will have to escape quickly.\nIt seems that the cargo elevator will arrive in some time\n\nOptions:\nRun\nCheck elevator\nShoot")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "RUN":
        C7FightR1()
    elif Select == "CHECK ELEVATOR":
        C7FightMove()
    elif Select == "SHOOT":
        C7FightS()
    else:
        print("Invalid command.")
        C7Start()

def C7FightMove():
    print("You move towards to the cargo elevator but you are shot.\n\nYou died.")
    input("Press enter to go back.")
    C7Start()

def C7FightR1():
    print("You run behind some more boxes.\nYou fire some shots.\nThe cargo elevator will arrive soon.\n\nOptions:\nRun\nCheck elevator\nShoot")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "RUN":
        C7FightR2()
    elif Select == "CHECK ELEVATOR":
        C7Ele()
    elif Select == "SHOOT":
        C7FightS2()
    else:
        print("Invalid command.")
        C7FightR1()
        
def C7FightS():
    print("You shoot back and you quickly run towards some boxes.\nIt seems the cargo elevator will take awhile.\n\nOptions:\nRun\nCheck elevator\nShoot")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "RUN":
        C7FightR2()
    elif Select == "CHECK ELEVATOR":
        C7Ele()
    elif Select == "SHOOT":
        C7FightS2()
    else:
        print("Invalid command.")
        C7FightS()

def C7Ele():
    print("The elevator isn't here yet.\nYou run to some boxes.")
    C7FightR2()

def C7FightR2():
    print("You run behind some more boxes and the cargo elevator arrives!\n\nOptions:\nElevator")       
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ELEVATOR":
        C7Elevation2()
    else:
        print("Invalid command.")
        C7FightR2()
        
def C7FightS2():
    print("You shoot at the lights.\nYou cannot see anything but it seems that the cargo elevator has arrived.\n\nOptions:\nElevator")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ELEVATOR":
        C7Elevation1()
    else:
        print("Invalid command.")
        C7FightS2()

def C7Elevation1():
    print("You quickly run to the elevator and the elevator starts going down.\n\nOptions:\nGo down")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO DOWN":
        C7Down()
    else:
        print("Invalid command.")
        C7Elevation1()

def C7Elevation2():
    print("You shoot the lights and quickly enter the cargo elevator\nThe doors quickly close and you start going down\n\nOptions:\nGo down")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GO DOWN":
        C7Down()
    else:
        print("Invalid command.")
        C7Elevation2()

def C7Down():
    print("The cargo lift slowly goes down and the doors eventually open.\nYou see someone shooting people.\nYou duck behind a box and you see Richard!\nYou call to him and he runs behind the box next to you.\n\nHe tells you to brace yourself.\n\nOptions:\nGet ready")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "GET READY":
        C7Explosion()
    else:
        print("Invalid command.")
        C7Down()

def C7Explosion():
    print("Richard throws a grenade hits the close doors.\nAbout 5 seconds later you hear a loud bang.\nThe doors seem jammed.\nYou decide to go to next floor up\n\nOptions:\nOpen doors")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "OPEN DOORS":
        C7Aftermath()
    else:
        print("Invalid command.")
        C7Explosion()


def C7Aftermath():
    print("You look down the stairs and the lower floor seems to be engulfed in fire.\nYou walk back to Richard.\nHe asks you if you have seen Emma.\nRichard tells you he rigged the place with cammera's but he hasn't saw anyone\nHe shows you floor plans, You quickly realise that the building is larger than you thought, you are about 3 quarters of the way up.\n\nOptions:\nLook for stairs")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LOOK FOR STAIRS":
        C7Change()
    else:
        print("Invalid command.")
        C7Aftermath()

def C7Change():
    print("Richard teels you that security from here is tight and he hands you a desiguse to put to on.\nRichard leaves the room while you change.\n\nOptions:\nWear Disguise")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WEAR DISGUISE":
        C7Disguise()
    else:
        print("Invalid command.")
        C7Change()

def C7Disguise():
    print("You change into the disguise but the building quickly goes into lockdown mode with an announcement stating that the building is compromised.\n\nRichard says that storming the CEOs room would be suicide so we should go to floor 8 instead of 9\nThe stairs are in the next room.\n\nOptions:\nLeave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C7Stairs()
    else:
        print("Invalid command.")
        C7Disguise()

def C7Stairs():
    print("You open the door and you are quickly greeted by security.\nYou show them your id's and you tell them that the intruders are on floor 2.\nThey quickly rush past you so you go up the stairs.\nAs you reach the next floor Richard gives you some explosives that he found on the 5th floor.\n\nOptions:\nFloor 7")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "FLOOR 7":
        C7Floor7()
    else:
        print("Invalid command.")
        C7Stairs()
        
def C7Floor7():
    print("You get to floor 7\nPeople are checking rooms, it seems it would be best to blend in here as it seems it will only be a matter of time before you are spotted.\n\nOptions:\nSneak through")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SNEAK THROUGH":
        C7Sneak()
    else:
        print("Invalid command.")
        C7Floor7()

def C7Sneak():
    print("Richard opens a door and shouts He's here!\nPeople crowd around the door and you quickly lock it once everyone was inside.\nRichard says the room is close.\n\nOptions:\nKeep walking")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KEEP WALKING":
        C7Walk()
    else:
        print("Invalid command.")
        C7Sneak()

def C7Walk():
    print("You see someone guarding the door.\nYou decide to shoot them but the camera has spotted you.\nYou quickly realise your cover is blown.\n\nOptions:\nEnter room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER ROOM":
        C7Rooms()
    else:
        print("Invalid command.")
        C7Walk()

def C7Rooms():
    print("You put your hand on the handle but Ricard tells you to wait.\nHe tells you that there might be a lot of people as this is an armoury.\nHe hands you a Rifle and a couple of clips.\n\nYou see some people that seem to be security.\nThey run towards you but the rifle seems to have explosive bullets.\nBesides that the room is empty.\nRichard starts taking some stuff from the walls.\nIt's mostly bight purple after he puts them in his bag a loud announcement is made.\nUnauthorized people in the armoury leathal force is authorised.\n\nOptions:\nLeave")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE":
        C7Explain()
    else:
        print("Invalid command.")
        C7Rooms()

def C7Explain():
    print("You run towards a storage cupboard.\nYou hide and Richard is still rumaging through a backpack but he zips it shut.\nYou both decide to wait a couple of minutes before leaving\nRichard shows you a kind of futureistic gun and tells you that you are now going to the 8th floor.\n\nThe room is silent.\n\nOptions:\nLeave room")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ROOM":
        C7Arm2()
    else:
        print("Invalid command.")
        C7Explain()

def C7Arm2():
    print("You leave the room and Richard tells you that the stairs are up ahead.\nAs you leave the room you decide to grab a few more guns and some ammo.\n\nYou get to the door but it seems that some people are waiting to ambush you.\n\nYou decide it would be better to take a detour.\n\nOptions:\nLeave Armoury")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ARMOURY":
        C7ArmCorridoor()
    else:
        print("Invalid command.")
        C7Arm2()

def C7ArmCorridoor():
    print("Richard opens the door and the corridoor is suprisingly empty.\nAccording to the floor plans there is an elevator nearby.\n\nOptions:\nCheck elevator")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CHECK ELEVATOR":
        C7ChkEle()
    else:
        print("Invalid command.")
        C7ArmCorridoor()

def C7ChkEle():
    print("As you turn the corner you hear the elevator.\nIt seems some one has arrived.\nRichard points the strange gun at the elevators.\nAs the soon as the door opens Richard pulls the trigger.\nThe gun releases a kind of laser beam.\nIt seems that the people in elevator were heavily armoured but laser beam seemed to disintrigrate it.\nYou clear out the elevator as it seems to still work.\n\nOptions:\nEnter Elevator")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER ELEVATOR":
        C7Lift()
    else:
        print("Invalid command.")
        C7ChkEle()

def C7Lift():
    print("You enter the elevator and you start going to floor 8.\nRichard starts looking at floor plans and compairing them.\nHe then circles a room and tells you thats where you are going.\n\nYou decide to ask why and he tells you it's under the CEOs room and that you could ambush him.\n\nOptions:\nLeave elevator")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LEAVE ELEVATOR":
        C7End()
    else:
        print("Invalid command.")
        C7Lift()

def C7End():
    print("Richard points the gun at the door incase anyone is waiting.\nNobody is.\nRichard opens a door and says this is the VP's room.\nSince the VP is dead it seems like the room has been cleared as most of the room is empty\nRichard says this is perfect.\n\n\n\nThis is final battle...\nYou can revisit old places if you wish.\n\nAre you ready?\n\nYes\nNo")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "YES":
        C8Start()
    elif Select == "NO":
        CSMnu()
    else:
        print("Invalid command.")
        C7End()

def CSMnu():
    print("Richard hands you a map.\nIt has a list of all the major places you have been.\n\nOptions:\nLucian Falls\nLibrary\nPolice Station\nShops\nEmmas house\nLucian Bunker\nUnderground town\nComputer Lab\nTech Bunker\nMechanical building\n\nThe final fight")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "LUCIAN FALLS":
        CSLF()
    elif Select == "LIBRARY":
        CSLib()
    elif Select == "POLICE STATION":
        CSPS()
    elif Select == "EMMAS HOUSE":
        CSEH()
    elif Select == "LUCIAN BUNKER":
        CSLB()
    elif Select == "UNDERGROUND TOWN":
        CSUT()
    elif Select == "COMPUTER LAB":
        CSCL()
    elif Select == "TECH BUNKER":
        CSTB()
    elif Select == "MECHANICAL BUILDING":
        CSMB()
    elif Select == "THE FINAL FIGHT":
        C8Start()
    else:
        print("Invalid command.")
        CSMnu()

def CSLF():
    print("You go to your old appartment.\n\nIt seems ransacked but your cat seems fine.\nThe cat keeps meowing at you but you give it some milk and food and prepare to leave.")
    CSMnu()

def CSLib():
    print("You look at the library but its just a pile of rubble.")
    CSMnu()

def CSPS():
    print("You look at the library but its just a pile of rubble.")
    CSMnu()

def CSEH():
    print("Emma's house seems empty but her pet is there they collar reads... sure?\n\nYou feed it and get ready to leave")#YOU DID THIS CAKESBAKED!!!
    CSMnu()

def CSLB():
    print("It looks destroyed.\nProbably best not to go inside.")
    CSMnu()

def CSUT():
    print("The town as completly vanished?")
    CSMnu()

def CSCL():
    print("You see that the lab has completly be burned to the ground.")
    CSMnu()

def CSTB():
    print("You enter the tech bunker and the teleporter has been disabled.")
    CSMnu()

def CSMB():
    print("The bunker has been evacuated.")
    CSMnu()

def C8Start():          #Right boys this is the hour of innevitable completion. By the way if your reading this nice one. I originally planned a way different version of the final boss battle it is now a bad ending further more I planned a web verion but github won't host stuff like that.
    print("Richard hands you a plasma gun.\nYou count from 3.\nRichard shoots and the floor disintigrates he throws you some rope and you start climbing up\n\nOptions:\nEnter Office")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER OFFICE":
        C8SOffice()
    else:
        print("Invalid command.")
        C8Start()

def C8SOffice(): #IT WAS A SETUP
    print("You look around.\nNobody is here.\n\nSuddenly you are surrounded by atleast 200+ people.\nThere is no way out.\n\nIs this the end, you ask Richard.\nThe only thing you hear back is It seems so.\n\nOptions:\nSurrender?")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "SURRENDER?":
        C8Surrender()
    elif Select == "SURRENDER":
        C8Surrender()
    else:
        print("Invalid command.")
        C8SOffice()

def C8Surrender():  # or was it.
    print("One of them asks you any last words?\nBefore you can even speak the room is full of bullets.\n\nA few seconds later you realise you are still alive.\nThe bullets came from outside?\nYou turn to look and you see Emma is piloting a helicopter.\nYou decide to say suprise.\nThere are a couple of people that are still alive.\n\nOptions:\nQuestion")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "QUESTION":
        C8Question()
    else:
        print("Invalid command.")
        C8Surrender()

def C8Question():
    print("You point a gun at the person who asked you for your final words.\nYou decide to ask them where the CEO is.\n\nThey refuse to answer you.\nRichard shoots them.\n\nEmma thows somthing into the room.\n\nOptions:\nPickup device")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "PICKUP DEVICE":
        C8Emma()
    else:
        print("Invalid command.")
        C8Question()

def C8Emma():
    print("You pick up the device, it's a radio.\nShe says the CEO left in one of 4 helicopters a few minutes ago.\n\nMore people come in to the room\nRichard thows a grenade in the doorway to make it collaspe.\nEmma says people are coming from the roof in helicopters.\nRichard shoot a plasma beam at the roof and you throw your last rope upto the roof.\n\nOptions:\nClimb up")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CLIMB UP":
        C8Roof()
    else:
        print("Invalid command.")
        C8Emma()

def C8Roof():
    print("You climb up.\nThere are a couple of helicopter that havent noticed you.\nLots of people are jumping from them and are planning to raid the office.\nYou shoot 2 of the helicopters and they fly off but crash.\nEmma makes quick work of the rest of the people on the roof.\nYou decide to go to the VP's bedroom\n\nOptions:\nClimb down")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CLIMB DOWN":
        C8VPRoom()
    else:
        print("Invalid command.")
        C8Roof()

def C8VPRoom():
    print("You climb down into the VP's bedroom\nsuddenly you hear the windows break someone has thrown a grenade.\n\nOptions:\nThow back\nWait")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "THOW BACK":
        C8Grenade()
    elif Select == "WAIT":   #Bruh moment
        C8Wait()
    else:
        print("Invalid command.")
        C8VPRoom()

def C8Wait():   #Well what did you Expect
    print("You wait.\nThe grenade explodes.")
    Select = input()
    C8Start()

def C8Grenade():
    print("You thow the grenade back while Richard trys to talk to Emma.\nYou ask her to land to pick you up but there is an Anti-Aircraft turret on the roof.\n\nOptions:\nRoof")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ROOF":
        C8RoofTurret()
    else:
        print("Invalid command.")
        C8Grenade()    

def C8RoofTurret():
    print("You get to the roof.\nYou see that the AA turret is relentlessly firing at Emma's Helicopter.\nYou decide to fire a plasma shot at it.\nEmma starts to land the helicopter.\n\nOption:\nEnter Helicopter")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "ENTER HELICOPTER":
        C8Heli()
    else:
        print("Invalid command.")
        C8RoofTurret()

def C8Heli():
    print("As you get in the helicopter Richard throws his last grenade into the stairs.\n\nEmma starts following one of the helicopters\nShe says the CEO is in that Helicopter.\n\nSuddenly you hear someone announce Goodbye Richard.\nSuddenly the back of the helicopter explodes!.\n\nYou are really close to the helicopter now so you might be able take down the Helicopter.\n\nOptions:\nExplosive bullets\nUsed explosives\nHelicopter Weapons")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "EXPLOSIVE BULLETS":
        C8G()
    elif Select == "HELICOPTER WEAPONS":
        C8HeliWeaps()
    elif Select == "USED EXPLOSIVES":
        C8Explo()
    else:
        print("Invalid command.")
        C8Heli()

def C8HeliWeaps():
    print("The helicopter spins out and you die.")
    input()
    C8RoofTurret()

def C8Explo():  #Bad ending one
    print("You try and use the used explosives but the don't explode.\nEmma only just manages to land the helicopter.\n\nWith the CEO escaping nobody knows what will happen now.\n")
    print("You have got the bad ending.\n\nGo back?\n\nYes\nNo")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "YES":
        print("Very well, Select the bullets.\nPress enter to continue")
        input()
        C8Heli()
    elif Select == "NO":
        print("Very well.")
        CSMenu()
    else:
        print("Invalid command.")
        C8Explo()    

def C8G():
    print("You shoot the blades of the helicopter\nThe CEO crashes into a few houses.\nEmma lands next to the CEOs Helicopter.\n\nOptions:\nConfront CEO")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "CONFRONT CEO":
        C8Confront()
    else:
        print("Invalid command.")
        C8G()

def C8Confront():
    print("The CEO points a plasma rifle at you and shoots the roof above you.\nEmma shoot him with her pistol.\nYou find a way past the rubble.\nThis is your chance to end it all.\nOptions:\nKill him\nAsk Questions\nSpare him")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "KILL HIM":
        C8GrandeFinale()
    elif Select == "ASK QUESTIONS":
        C8Questions()
    elif Selcet == "SPARE HIM":
        C8Spare()
    else:
        print("Invalid command.")
        C8Confront()

def C8Spare():
    print("A wise desicion Lucas.\nHe shoots the ground underneath you.\nYou hear him call for an ambulance and you feel like your being dragged somewhere.")
    print("You have got the bad ending.\n\nGo back?\n\nYes\nNo")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "YES":
        print("Very well, Finish the job then.\nPress enter to continue")
        input()
        C8Spare()
    elif Select == "NO":
        print("Very well.")
        CSMenu()
    else:
        print("Invalid command.")
        C8Explo()    

def C8Questions():
    print("You decide to keep him alive for a few more minutes.\nHe reaches for the plasma gun but you kick it out of reach and tell him Nice try.\n\nYou wonder what to ask him.\n\nQuestions:\nWhat are your plans?\nHow did you make the Rocket?\nWho is the VP?\nHow did you get a teleporter?\nWhat happened to Emma?\nWhy target Lucian Falls?\n\nContinue")
    Select = input()
    Select = Select.upper()
    print("")
    if Select == "WHAT ARE YOUR PLANS?":
        C8FQPlans()
    elif Select == "HOW DID YOU MAKE THE ROCKET?":
        C8FQRocket()
    elif Select == "WHO IS THE VP?":
        C8FQVP()
    elif Select == "HOW DID YOU GET A TELEPORTER?":
        C8FQTP()
    elif Select == "WHY TARGET LUCIAN FALLS?":
        C8FQLF()
    elif Select == "WHAT HAPPENED TO EMMA?":
        C8FQEmma()
    elif Select == "CONTINUE":
        C8FQcont()
    else:
        print("Invalid Question.")
        C8Questions()

def C8FQPlans():
    print("My plan is to run this country however it seems it was easier to corrupt people than we anticipated.")
    C8Questions()

def C8FQRocket():
    print("The rocket was a really good distraction while I finished up corrupting the authorites.")
    C8Questions()

def C8FQEmma():
    print("Well we tryed to ransom her but that all failed when she stole a experemental pistol.")
    C8Questions()

def C8FQLF():
    print("We had a secret lab under there and we needed to secure it.")
    C8Questions()

def C8FQVP():
    print("He was a close personal friend and a genius buisness man, it was his idea to create the rocket.\nIt's why I had everyone here once I learned that you easily killed him.\nBut here we are.")
    C8Questions()

def C8FQTP():
    print("We didn't.\nThe military already have them we just corrupted the top officals and now they are funding us and giving us lots of teleporters.")
    C8Questions()

def C8FQcont():
    print("He is dying... You decide to ask him two more questions\n\nOptions:\nWhy did you break technology?")
    if Select == "WHY DID YOU BREAK TECHNOLOGY?":
        C8FinaleQ1()
    else:
        print("Invalid command.")
        C8FQcont()

def C8FinaleQ1():
    print("For over a decade the militiary have been mandating an invisible kill switch into all technology.\nWhen I found out the VP told me my eyes lit up.\nI also made military grade EMPs and this would pave the way to my final plan.\n\nOptions:\nWhat is your final plan")
    if Select == "WHAT IS YOUR FINAL PLAN":
        C8FinaleLastSuprise()
    else:
        print("Invalid command.")
        C8FinaleQ1()

def C8FinaleLastSuprise():
    print("Well a magician never reveals his secrets so neither will I.\nMy death is pointless and I will be replaced.\n\nKill him\nSpare him")
    if Select == "KILL HIM":
        C8GrandeFinale()
    elif Select == "SPARE HIM":
        C8Spare()
    else:
        print("Invalid command.")
        C8FinaleLastSuprise()

def C8GrandeFinale():
    print("See you in hell, Lucas.\n\nYou shoot him.\n\nA huge burden has been lifted from your sholders.\nBut the final fight has only just begun.")
    print("\n\nCongratulations.\n\nTyping Chapter select at the title screen will allow you to select a chapter.\n\nThank you.\nCreated by TMAltair and Cakesbaked.")
    input("Press enter to go to chapter select")
    CSChapSel()
#Starting Function
CSMenu()
#Stops program from crashing/closing due to an error or complete execution

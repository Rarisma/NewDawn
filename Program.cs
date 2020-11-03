//NewDawn Engine C# Edition by Rarisma
//No line 2
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Threading;

namespace NewDawn_Engine_CSharp
{
    public class System //Stores variables that aren't local to a function
    {
        public static string Path = AppDomain.CurrentDomain.BaseDirectory; //Gets the executing directory
        public static char SlashType = Path.Last(); //Will get the type of slash (Prevents crashing on Unix Based system as / is used instead of \)
        
        //Stores Engine Data (Frequently Changed during code execution)
        public static string RoomPath; //Stores the path to the room folder (Includes Slash)
        public static List<string> Links = new List<string>(); //Links are the names of folders (ID corresponds with Options)
        public static List<string> Options = new List<string>(); //Options are shown to the user and when selected sends the user to the corresponding link
        public static string[] EngineInfo = { "Example Game", "1", "Start", "0" }; //EngineInfo stores the locations of file  - EngineInfo {0 - Game Name 1-ChapterID, 2-RoomID, 3-OptionType (0 is over 10 options, 1 is less than 10)

        //Stores UserData
        public static string[] TextVar = { "", "", "", "", "", "" }; //Text array for engine variable
        public static bool[] BoolVar = { false, false, false, false, false }; //Boolean Variable for engine variable
    }

    public class ErrorCheck // Stores all functions that
    {
        public static bool CheckDataFolder() // Freezes game if it cannot find any games or if \Data\ is missing
        {
            if (Directory.Exists(System.Path + System.SlashType + "Data") == false)
            {
                Console.WriteLine("Hey!\nYou are missing the Data folder!\n\nThis means you have no games downloaded.\nTo get some games please download the Data.7z on the NewDawn GitHub\n\nPress enter to quit");
                Console.ReadLine();
                Environment.Exit(0);
            }
            else
            {
                string[] Test;
                try
                {
                    Test = Directory.GetDirectories(System.Path + System.SlashType + "Data"); // This gets the full path to each directory in data
                }
                catch
                {
                    Console.WriteLine("Oh No!\nYou have no games!\nYou can download some sample games from the NewDawn Github\n\nPress enter to quit");
                    Console.ReadLine();
                    Environment.Exit(0);
                }
            }
            return true;
        }
    
        public static bool CriticalFileCheck() // Checks for O/L/T.txt files or if ChapterChange.txt exists
        {
            if (File.Exists(System.RoomPath + "T.txt") && File.Exists(System.RoomPath + "O.txt") && File.Exists(System.RoomPath + "L.txt")) // Checks that all rooms exist and throws an error to check
            {
                Thread.Sleep(0);
            }
            else
            {
                if (File.Exists(System.RoomPath + "ChapterChange.txt") == true) // Checks if a chapter Change exists
                {
                    string[] Temp = File.ReadAllLines(System.RoomPath + "ChapterChange.txt");
                    System.EngineInfo[1] = Temp[0];
                    System.EngineInfo[2] = "Start";
                    NewEngine.EngineCheck();
                }
                else
                {
                    Console.WriteLine("A Critical file is missing from this room\n If you are the developer please check that O.txt, L.txt and T.txt exists in,\n" + System.RoomPath + "\nPress enter to be sent back to the main menu\n\nSTATUS REPORT:\nT.txt is present " + File.Exists(System.RoomPath + "T.txt") + "\nL.txt is present " + File.Exists(System.RoomPath + "L.txt") + "\nO.txt is present " + File.Exists(System.RoomPath + "O.txt"));
                    Console.Read();
                    Program.Main();
                }
            }
            return true;
        }
        
        public static bool OptionLinkCheck(int a, int b)
        {
            if (a != b)//Checks room is valid
            {
                Console.WriteLine("This room is incorectly configured as it doesn't have the same lines in o.txt and l.txt\nIf you are not the developer you should report this,\n\nPress Enter to be sent back to the main menu.\n\nStatus Report:\n" + "Links:"  + a + "\nOptions: " + b); //If you are a dev and this happens you should feel bad.
                Console.ReadLine();
                Program.Main();
            }
            else
            {
                return true;
            }
            return true;
        }
    }

    public class CommonCode //Wadya know this stores common functions to save space
    {
        public static int IntInput() //Gets input and then turns it into a interger and handles all error checking
        {
            int Passback = -1;
            bool loop = true;
            while (loop == true)
            {
                try
                {
                    string StringInput = Console.ReadLine(); //Gets a readline input
                    Passback = Convert.ToInt32(StringInput); //Converts StringInput to passback (Will error if wrong)
                    if (Passback > 9 )
                    {
                        Console.WriteLine("Enter a number from 1-9 (Includes 0)");
                    }
                    else 
                    {
                        loop = false;
                    }
                }
                catch
                {
                    Console.WriteLine("That is not a number");
                    loop = true;
                }
            }
            return Passback;
        }
    }

    class Program // Stores the main menu
    {
        public static void Main() //Main stores the menu
        {
            Console.WriteLine("NewDawn Engine 0.2.0 (C# Edition)\n\n1) Load Game\n0) Quit" ); //Prints menu 
            int Input = CommonCode.IntInput();
            Console.WriteLine(Input);
            
            if (Input == 1) // If 1 is entered
            {
                Console.Clear();//Clears the screen
                Console.WriteLine("Select a game:\n");
                ErrorCheck.CheckDataFolder();  
               
                string[] GameDirs = Directory.GetDirectories(System.Path + System.SlashType + "Data");  // This gets the full path to each directory in data
                for (int i = 0; i <= GameDirs.Length - 1; i++) //Prints the name of every directory in /data/
                {  
                    Console.WriteLine(i + ") " + Path.GetFileName(GameDirs[i])); //Path.GetFileName gets the name of the final folder in a path
                }
                Console.WriteLine("Press Enter when you are done.\n");
                Thread.Sleep(1000);

                while (1 == 1) //This loop lets the User pick a game then loads it (Perma loop btw)
                {
                    try
                    {
                        Thread.Sleep(100);
                        System.EngineInfo[0] = Path.GetFileName(GameDirs[Convert.ToInt32(Console.ReadLine())]); //gets name of game
                        System.EngineInfo[1] = "1";
                        System.EngineInfo[2] = "Start";
                        Console.Clear();
                        NewEngine.NFOMenu();
                    }
                    catch //This should only be executed if there is a input that isn't a interger (or if somthing goes wrong)
                    {
                        Console.WriteLine("Please enter a valid number, Shown in brackets\nSuch as 1)"); //Helpful message
                    }
                }                
            }
            else if (Input == 0)
            {
                Environment.Exit(0); //Exits Safely
            }
        }
    }

    class NewEngine //Newer version of the engine
    {
        public static void NFOMenu() //Turns NFO files into a custom main menu
        {
            string[] NFO = File.ReadAllLines(System.Path + "data" + System.SlashType + System.EngineInfo[0] + System.SlashType + "i.nfo");
            Console.WriteLine(NFO[0] + "   (" + NFO[3] + ")" + "\n1) Play\n2) Load Game - UNAVAILABLE\n0) Back to Main menu\n\nRelease Date: " + NFO[4] + "\n" + NFO[2]);

            int Input = CommonCode.IntInput();
            if (Input == 1)
            {
                EngineCheck();
            }
            else if (Input == 0)
            {
                Program.Main();
            }
        }

        public static void EngineCheck() //This checks that the room is valid and sets up options and links
        {
            System.RoomPath = System.Path + "Data" + System.SlashType + System.EngineInfo[0] + System.SlashType + System.EngineInfo[1] + System.SlashType + System.EngineInfo[2] + System.SlashType; //Stores the path to the current room
            System.Links.Clear(); //Clears all items in Links
            System.Options.Clear();
            Console.Clear();
            ErrorCheck.CriticalFileCheck(); //Will throw error is a critical file is missing

            System.Options.AddRange(File.ReadAllLines(System.RoomPath + "O.txt")); //Adds each line in O.txt as a individual item in the list
            System.Links.AddRange(File.ReadAllLines(System.RoomPath + "L.txt")); //Adds each line in O.txt as a individual item in the list
            ErrorCheck.OptionLinkCheck(System.Links.Count, System.Options.Count); //Compares size of Options and Links, if different throws error

            if (File.Exists(System.RoomPath + "ChapterChange.txt") == true) // Checks if a chapter Change exists
            {
                string[] Temp = File.ReadAllLines(System.RoomPath + "ChapterChange.txt");
                System.EngineInfo[1] = Temp[0];
                System.EngineInfo[2] = "Start";
                NewEngine.EngineCheck();
            }

            if (File.Exists(System.RoomPath + "VarSet.txt") || File.Exists(System.RoomPath + "VarCheck.txt")) //Only sends user to Variables if the files exist
            {
                NewEngine.Variables();
            }
            else //Otherwise just builds the room
            {
                NewEngine.BuildRoom();
            }
        }

        public static void Variables() //This function handles Varset and VarCheck
        {
            string[] TempFile; //Used as a temporary file reader
            if (File.Exists(System.RoomPath + "VarSet.txt")) // This Sets Variables
            {
                Console.WriteLine("Varset");
                Thread.Sleep(5000);
                TempFile = File.ReadAllLines(System.RoomPath + "VarSet.txt"); // (0 - bool/text  1 - Place in array   2 - Value)
                if (TempFile[0] == "bool")
                {
                    if (TempFile[2] == "false")
                    {
                        System.BoolVar[Convert.ToInt32(TempFile[1])] = false;
                    }
                    else if (TempFile[2] == "true")
                    {
                        System.BoolVar[Convert.ToInt32(TempFile[1])] = true;
                    }
                }
                else if (TempFile[0] == "text")
                {
                    System.TextVar[Convert.ToInt32(TempFile[1])] = TempFile[2];
                }
            }

            if (File.Exists(System.RoomPath + "VarCheck.txt"))// Checks Variables
            {//0-text/bool 1-Position in array 2-expected result 3-Positive Result Option 4- Positive result link
                Console.WriteLine("VarCheck");
                TempFile = File.ReadAllLines(System.RoomPath + "VarCheck.txt");
                if (TempFile[0] == "bool")
                {
                    if (TempFile[2] == Convert.ToString(System.BoolVar[Convert.ToInt32(TempFile[1])])) //Converts sp
                    {
                        System.Options.Add(TempFile[3]);
                        System.Links.Add(TempFile[4]);
                    }
                }
                else if (TempFile[0] == "text")
                {
                    if (TempFile[2] == Convert.ToString(System.TextVar[Convert.ToInt32(TempFile[1])])) //Converts sp
                    {
                        System.Options.Add(TempFile[3]);
                        System.Links.Add(TempFile[4]);
                    }
                }
            }

            NewEngine.BuildRoom(); //Sends user to build room if theres an error or when done
        }

        public static void BuildRoom() //Outputs Room
        {
            Console.WriteLine(File.ReadAllText(System.RoomPath + "T.txt") + "\nOptions:\n"); //This prints all the t.txt file
            for (int i = 1; System.Options.Count >= i; i++)
            {
                Console.WriteLine(i + ") " + System.Options[i - 1]); // Offsets option by one to account for keyboards being 1,9 + 0
            }

            NewEngine.UserInput();
        }

        public static void UserInput()
        {
            int Input = CommonCode.IntInput();
            if (Input == 0 && System.Links.Count == 8)
            {
                System.EngineInfo[2] = System.Links[8];
            }
            else if (Input == 1 || Input == 2 || Input == 3 || Input == 3 || Input == 4 || Input == 5 || Input == 6 || Input == 7 || Input == 8 || Input == 9)
            {
                System.EngineInfo[2] = System.Links[Input - 1];
            }
            else //Couldn't fix an error so this just prevents a crash
            {
                Console.Clear();
                Console.WriteLine("It seems like an error occurred. Sorry!\nThe console will recover in 5 seconds...");
                Thread.Sleep(5000);
                NewEngine.EngineCheck();
            }
            NewEngine.EngineCheck(); //Completes the loop, by sending the user back to engine check
        }
    }
}
//The horrors of the night melt away, under the warm glow of survival of the day 

//NewDawn Engine C# Edition by Rarisma
//Smoothbrain tried to stop me last time (Dec 23rd)
//
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;
using System.Net;
using System.IO.Compression;
using System.Diagnostics;

namespace NewDawn_Engine_CSharp
{
    public class Global //Stores variables that aren't local to a function
    {
        public static string Path = AppDomain.CurrentDomain.BaseDirectory; //Gets the executing directory
        public static char SlashType = Path.Last(); //Will get the type of slash (Prevents crashing on Unix Based system as / is used instead of \)
        public static bool DevMode = true; // Disable for release builds

        //Stores Engine Data (Frequently Changed during code execution)
        public static string RoomPath; //Stores the path to the room folder (Includes Slash)
        public static List<string> Links = new List<string>(); //Links are the names of folders (ID corresponds with Options)
        public static List<string> Options = new List<string>(); //Options are shown to the user and when selected sends the user to the corresponding link
        public static string[] EngineInfo = { "Example Game", "1", "Start", "0" }; //EngineInfo stores the locations of file  - EngineInfo {0 - Game Name 1-ChapterID, 2-RoomID, 3-OptionType (0 is over 10 options, 1 is less than 10)

        //Stores UserData
        public static List<string?> TextVar = new List<string?>();  //Text array for engine variable
        public static List<bool?> BoolVar = new List<bool?>(); //Boolean Variable for engine variable
    }

    public class Common //Wadya know this stores common functions to save space
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
        public static bool CheckDataFolder() // Freezes game if it cannot find any games or if \Data\ is missing
        {
            if (Directory.Exists(Global.Path + Global.SlashType + "Data") == false)
            {
                Console.WriteLine("Hey!\nYou are missing the Data folder!\n\nThis means you have no games downloaded.\nTo get some games please download the Data.7z on the NewDawn GitHub\n\nPress enter to quit");
                Console.ReadLine();
                Environment.Exit(0);
            }
            else
            {
                try
                {
                    string[] Test = Directory.GetDirectories(Global.Path + Global.SlashType + "Data"); // This gets the full path to each directory in data
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
            if (File.Exists(Global.RoomPath + "T.txt") && File.Exists(Global.RoomPath + "O.txt") && File.Exists(Global.RoomPath + "L.txt")) // Checks that all rooms exist and throws an error to check
            {
                Thread.Sleep(0);
            }
            else
            {
                if (File.Exists(Global.RoomPath + "ChapterChange.txt") == true) // Checks if a chapter Change exists
                {
                    string[] Temp = File.ReadAllLines(Global.RoomPath + "ChapterChange.txt");
                    Global.EngineInfo[1] = Temp[0];
                    Global.EngineInfo[2] = "Start";
                    NewEngine.EngineCheck();
                }
                else
                {
                    Console.WriteLine("A Critical file is missing from this room\n If you are the developer please check that O.txt, L.txt and T.txt exists in,\n" + Global.RoomPath + "\nPress enter to be sent back to the main menu\n\nSTATUS REPORT:\nT.txt is present " + File.Exists(Global.RoomPath + "T.txt") + "\nL.txt is present " + File.Exists(Global.RoomPath + "L.txt") + "\nO.txt is present " + File.Exists(Global.RoomPath + "O.txt"));
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
                Console.WriteLine("This room is incorectly configured as it doesn't have the same lines in o.txt and l.txt\nIf you are not the developer you should report this,\n\nPress Enter to be sent back to the main menu.\n\nStatus Report:\n" + "Links:" + a + "\nOptions: " + b); //If you are a dev and this happens you should feel bad.
                Console.ReadLine();
                Program.Main();
            }
            else
            {
                return true;
            }
            return true;
        } //Checks Length of Options and Links to prevent errors
    
        public static string DLExtract(string ZipURL, string ExtractionPath) //Downloads a Zip and Extracts it + handles UI
        {
            Console.Clear(); //Clears Screen for Clarity
            Console.WriteLine("Initalising Download (1/4)");

            using (var client = new WebClient()) // Downloads File
            { //ZipURL is a URL to a ZipFile    ExtractionPath is a folder path
                client.DownloadFile(ZipURL, Global.Path + "Download.zip");
            }

            Console.WriteLine("Download Complete!\nExtracting files... (2/3)");
            ZipFile.ExtractToDirectory(Global.Path + Global.SlashType + "Download.zip", ExtractionPath); //Turns out ZipFile Really means Zip File

            Console.WriteLine("Extraction Complete\nCleaning Up (3/3)");
            File.Delete(Global.Path + Global.SlashType + "Download.zip");

            Console.WriteLine("Complete\nPress enter to continue");

            return "a";
        }
    }

    class Program // Stores the main menu
    {
        public static void Main() //Main stores the menu
        {
            Console.WriteLine("NewDawn Engine 0.2.0 (C# Edition)\n\n1) Load Game\n2) Update\n3) Download New Games\n0) Quit" ); //Prints menu 
            int Input = Common.IntInput();

            if (Input == 1) // If 1 is entered
            {
                Console.Clear();//Clears the screen
                Common.CheckDataFolder();
                Console.WriteLine("Select a game:\n");

                string[] GameDirs = Directory.GetDirectories(Global.Path + Global.SlashType + "Data");  // This gets the full path to each directory in data
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
                        Global.EngineInfo[0] = Path.GetFileName(GameDirs[Convert.ToInt32(Console.ReadLine())]); //gets name of game
                        Global.EngineInfo[1] = "1";
                        Global.EngineInfo[2] = "Start";
                        Console.Clear();
                        NewEngine.NFOMenu();
                    }
                    catch //This should only be executed if there is a input that isn't a interger (or if somthing goes wrong)
                    {
                        Console.WriteLine("Please enter a valid number, Shown in brackets\nSuch as 1)"); //Helpful message
                    }
                }
            }
            else if (Input == 2)
            {
                Updater();
            }
            else if (Input == 3)
            {
                Console.WriteLine("Select a game to download: ");

                using (var client = new WebClient()) // Downloads File
                { //ZipURL is a URL to a ZipFile    ExtractionPath is a folder path
                    client.DownloadFile("https://raw.githubusercontent.com/Rarisma/NewDawn/master/Downloader/index.txt", Global.Path + "index.txt");
                }

                string[] Games = File.ReadAllLines(Global.Path + Global.SlashType + "index.txt");


                


            }
            else if (Input == 0)
            {
                Environment.Exit(0); //Exits Safely
            }
        }
    
        public static void Updater()
        {
            Common.DLExtract("https://github.com/Rarisma/NewDawn/blob/master/Update/Data.zip?raw=true", Global.Path + "\\UPDATE\\");
            Console.WriteLine("An updated version of NewDawn has been downloaded, to use it go to the update folder and drag it into the base directory of NewDawn and click overwrite to update.\nYour saves will not be affected.");
        }
    }

    class NewEngine //Newer version of the engine
    {
        public static void NFOMenu() //Turns NFO files into a custom main menu
        {
            string[] NFO = File.ReadAllLines(Global.Path + "data" + Global.SlashType + Global.EngineInfo[0] + Global.SlashType + "i.nfo");
            Console.WriteLine(NFO[0] + "   (" + NFO[3] + ")" + "\n1) Play\n2) Load Game - UNAVAILABLE\n0) Back to Main menu\n\nRelease Date: " + NFO[4] + "\n" + NFO[2]);

            int Input = Common.IntInput();
            if (Input == 1)
            {
                int temp = 0;
                Global.BoolVar = new List<bool?>();
                Global.TextVar = new List<string?>();
                while (temp < 100000) // move this to system for readability at some point
                {//This nulls 1000 elements on BoolVar and TextVar
                    Global.BoolVar.Add(null);
                    Global.TextVar.Add(null);
                    temp += 1;
                }

                EngineCheck();
            }
            else if (Input == 0)
            {
                Program.Main();
            }
        }

        public static void EngineCheck() //This checks that the room is valid and sets up options and links
        {
            Global.RoomPath = Global.Path + "Data" + Global.SlashType + Global.EngineInfo[0] + Global.SlashType + Global.EngineInfo[1] + Global.SlashType + Global.EngineInfo[2] + Global.SlashType; //Stores the path to the current room
            Global.Links.Clear(); //Clears all items in Links
            Global.Options.Clear();
            Console.Clear();
            Common.CriticalFileCheck(); //Will throw error is a critical file is missing

            Global.Options.AddRange(File.ReadAllLines(Global.RoomPath + "O.txt")); //Adds each line in O.txt as a individual item in the list
            Global.Links.AddRange(File.ReadAllLines(Global.RoomPath + "L.txt")); //Adds each line in O.txt as a individual item in the list
            Common.OptionLinkCheck(Global.Links.Count, Global.Options.Count); //Compares size of Options and Links, if different throws error

            if (File.Exists(Global.RoomPath + "ChapterChange.txt") == true) // Checks if a chapter Change exists
            {
                string[] Temp = File.ReadAllLines(Global.RoomPath + "ChapterChange.txt");
                Global.EngineInfo[1] = Temp[0];
                Global.EngineInfo[2] = "Start";
                NewEngine.EngineCheck();
            }

            if (File.Exists(Global.RoomPath + "VarSet.txt") || File.Exists(Global.RoomPath + "VarCheck.txt")) //Only sends user to Variables if the files exist
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
            if (File.Exists(Global.RoomPath + "VarSet.txt")) // This Sets Variables
            {
                Console.WriteLine("Varset");
                Thread.Sleep(5000);
                TempFile = File.ReadAllLines(Global.RoomPath + "VarSet.txt"); // (0 - bool/text  1 - Place in array   2 - Value)
                if (TempFile[0] == "bool")
                {
                    if (TempFile[2] == "false")
                    {
                        Global.BoolVar[Convert.ToInt32(TempFile[1])] = false;
                        Console.WriteLine("Boolean Variable set at " + TempFile[1] + " With the value of False");
                    }
                    else if (TempFile[2] == "true")
                    {
                        Global.BoolVar[Convert.ToInt32(TempFile[1])] = true;
                        Console.WriteLine("Boolean Variable set at " + TempFile[1] + " With the value of True");
                    }
                }
                else if (TempFile[0] == "text")
                {
                    Global.TextVar[Convert.ToInt32(TempFile[1])] = TempFile[2];
                }
            }

            if (File.Exists(Global.RoomPath + "VarCheck.txt"))// Checks Variables
            {//0-text/bool 1-Position in array 2-expected result 3-Positive Result Option 4- Positive result link
                Console.WriteLine("VarCheck");
                TempFile = File.ReadAllLines(Global.RoomPath + "VarCheck.txt");
                if (TempFile[0] == "bool")
                {
                    Console.WriteLine("Boolean Check - BoolVar[" + TempFile[1] + "] == " + TempFile[2] + "Result: ");
                    Console.WriteLine(TempFile[2] == Convert.ToString(Global.BoolVar[Convert.ToInt32(TempFile[1])]));
                    Console.WriteLine(Convert.ToString(Global.BoolVar[Convert.ToInt32(TempFile[1])]));
                    Thread.Sleep(5000);
                    if (TempFile[2] == Convert.ToString(Global.BoolVar[Convert.ToInt32(TempFile[1])])) //Converts sp
                    {
                        Console.WriteLine("VarCheck Pass");
                        Global.Options.Add(TempFile[3]);
                        Global.Links.Add(TempFile[4]);
                    }
                }
                else if (TempFile[0] == "text")
                {
                    if (TempFile[2] == Convert.ToString(Global.TextVar[Convert.ToInt32(TempFile[1])])) //Converts sp
                    {
                        Console.WriteLine("VarCheck Pass");
                        Global.Options.Add(TempFile[3]);
                        Global.Links.Add(TempFile[4]);
                    }
                }
                else
                {
                    Console.WriteLine("VarCheck Failed");
                }
            }

            NewEngine.BuildRoom(); //Sends user to build room if theres an error or when done
        }

        public static void BuildRoom() //Outputs Room
        {
            Console.WriteLine(File.ReadAllText(Global.RoomPath + "T.txt") + "\nOptions:\n"); //This prints all the t.txt file
            for (int i = 1; Global.Options.Count >= i; i++)
            {
                Console.WriteLine(i + ") " + Global.Options[i - 1]); // Offsets option by one to account for keyboards being 1,9 + 0
            }

            NewEngine.UserInput();
        }

        public static void UserInput()
        {
            int Input = Common.IntInput();
            if (Input == 0 && Global.Links.Count == 8)
            {
                Global.EngineInfo[2] = Global.Links[8];
            }
            else if (Input == 1 || Input == 2 || Input == 3 || Input == 3 || Input == 4 || Input == 5 || Input == 6 || Input == 7 || Input == 8 || Input == 9)
            {
                Global.EngineInfo[2] = Global.Links[Input - 1];
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
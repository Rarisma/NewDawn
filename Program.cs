//NewDawn Engine C# Edition by Rarisma
//Coding in the booth with a tripple fat goose hazmat suit, bubble sort and subnet mask too and I don't think thats what they ment about Data Interception - Code To Be Executed by

using System;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.Design;
using System.IO;
using System.Linq;
using System.Reflection.PortableExecutable;
using System.Runtime.CompilerServices;
using System.Threading;

namespace NewDawn_Engine_CSharp
{
    public class System //Stores variables that aren't local to a function
    {
        public static string[] EngineInfo = { "Example Game", "1", "Start", "0" }; // Initalises EngineInfo {0 - Game Name 1-ChapterID, 2-RoomID, 3-OptionType (0 is over 10 options, 1 is less than 10)
        public static string Path = AppDomain.CurrentDomain.BaseDirectory; //Gets the executing directory
        public static char SlashType = Path.Last(); //Will get the type of slash (Prevents crashing on Unix Based system as / is used instead of \)
        public static string RoomPath; //Gets set by engine when initialised    
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
                    Engine.EngineInitalise();
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
                Console.WriteLine("This room is incorectly configured as it doesn't have the same lines in o.txt and l.txt\nIf you are not the developer you should report this,\n\nPress Enter to be sent back to the news"); //If you are a dev and this happens you should feel bad.
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
            Console.WriteLine("NewDawn Engine 0.1.3 (C# Edition)\n\n1) Load Game\n0) Quit"); //Prints menu 
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
                        Engine.NFOMenu();
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

    public class Engine // Stores Main code
    { 
        public static void NFOMenu() //Turns I.NFO into a menu that is easily made by I.Nfo
        {
            string[] NFO = File.ReadAllLines(System.Path + "data" + System.SlashType + System.EngineInfo[0] + System.SlashType + "i.nfo");
            Console.WriteLine(NFO[0] + "   (" + NFO[3] + ")" + "\n1) Play\n2) Load Game - UNAVAILABLE\n0) Back to Main menu\n\nRelease Date: " + NFO[4] + "\n" + NFO[2]);
            
            int Input = CommonCode.IntInput();
            if (Input == 1)
            {
                EngineInitalise();            
            }
            else if (Input == 0)
            {
                Program.Main();
            }
        }

        public static void EngineInitalise() //Initalises the engine (Performs error checking and loads data for room)
        {
            System.RoomPath = System.Path + "Data" + System.SlashType + System.EngineInfo[0] + System.SlashType + System.EngineInfo[1] + System.SlashType + System.EngineInfo[2] + System.SlashType; //Stores the path to the current room
            Console.Clear();
            if (ErrorCheck.CriticalFileCheck() == true) //Only contines if critical files are present
            {
                string[] OptionText = File.ReadAllLines(System.RoomPath + "O.txt"); //loops and prints each text with the id of the command
                string[] Links = File.ReadAllLines(System.RoomPath + "L.txt");  //Reads L.txt
                bool Temp = ErrorCheck.OptionLinkCheck(OptionText.Length,Links.Length); //Compares option links
                if (Temp == true)
                {
                    Engine.Output();
                }
            }
        }
        
        public static void Output() // Displays room options and handles user input
        {
            string[] OptionText = File.ReadAllLines(System.RoomPath + "O.txt"); //loops and prints each text with the id of the command
            string[] Links = File.ReadAllLines(System.RoomPath + "L.txt");  //Reads L.txt

            Console.WriteLine(File.ReadAllText(System.RoomPath + "T.txt") + "\nOptions:\n"); //This prints all the t.txt file
            for (int i = 1; OptionText.Length >= i; i++)
            {
                Console.WriteLine(i + ") " + OptionText[i - 1]); // Offsets option by one to account for keyboards being 1,9 + 0
            }

            int Input = CommonCode.IntInput();

            if (Input == 0 && Links.Length == 8)
            {
                System.EngineInfo[2] = Links[8];
            }
            else if (Input == 1 || Input == 2 || Input == 3 || Input == 3 || Input == 4 || Input == 5 || Input == 6 || Input == 7 || Input == 8 || Input == 9)
            {
                System.EngineInfo[2] = Links[Input - 1];
            }
            else //Couldn't fix an error so this just prevents a crash
            {
                Console.Clear();
                Console.WriteLine("It seems like an error occurred. Sorry!\nThe console will recover in 5 seconds...");
                Thread.Sleep(5000);
                EngineInitalise();
            }
            EngineInitalise();
        }
    }
}
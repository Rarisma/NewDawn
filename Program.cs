// NewDawn Engine C# Edition 0.1.1 by Rarisma
// Writing code like this reminds of SmallBasic (Fr tho wtf are those mascots bruh)
// **LUCAS OVERWRITES THE BATTLE**
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.Design;
using System.IO;
using System.Threading;

namespace NewDawn_Engine_CSharp
{
    public class SysVars
    {
        public static string[] EngineInfo = { "Example Game", "1", "Start", "0" }; // Initalises EngineInfo {0 - Game Name 1-ChapterID, 2-RoomID, 3-OptionType (0 is over 10 options, 1 is less than 10)
        public static string path = AppDomain.CurrentDomain.BaseDirectory; //Gets the executing directory

    }

    class Program
    {

        static void Main(string[] args) //Main stores the menu
        {
            string path = AppDomain.CurrentDomain.BaseDirectory; //Gets the executing directory
            string StrInput = "0"; //Stores the users option as a string but gets converted to IntInput
            int IntInput = 0; // Stores the user option as a Interger

            Console.WriteLine("NewDawn Engine 0.1.1 (C# Edition)\n\n1) Load Game\nE) Quit"); //Prints menu 

            if (Console.ReadKey().Key == ConsoleKey.D1) // This checks if 1 is pressed
            {
                Console.Clear();//Clears the screen
                Console.WriteLine("Select a game:\n");

                string[] GameDirs = Directory.GetDirectories(path + "\\Data"); // This gets the full path to each directory in data
                for (int i = 0; i <= GameDirs.Length - 1; i++) //Prints the name of every directory in /data/
                { //Prints and itterates though the name of each directory
                    Console.WriteLine(i + ") " + Path.GetFileName(GameDirs[i])); //Path.GetFileName gets the name of the final folder in a path
                }
                Console.WriteLine("Press Enter when you are done.\n");
                Thread.Sleep(1000);

                int loop = 1;
                while (loop == 1) //This loop lets the user select a game and then checks the input is valid (int)
                {
                    try
                    {
                        Thread.Sleep(100);
                        StrInput = Console.ReadLine();
                        IntInput = Convert.ToInt32(StrInput); //Could probably be done in a single line
                        SysVars.EngineInfo[0] = Path.GetFileName(GameDirs[IntInput]); //gets name of game
                        loop = 0;
                    }
                    catch (Exception) //This should only be executed if there is a input that isn't a interger (or if somthing goes wrong)
                    {
                        Console.WriteLine("Please enter a number, Shown in brackets\nSuch as 1)"); //Helpful message
                    }
                }
                Console.WriteLine("Now Loading " + Path.GetFileName(GameDirs[IntInput])); // Displays game name while loading
                SysVars.EngineInfo[1] = "1";
                SysVars.EngineInfo[2] = "Start";
                Program.Engine();
            }
        }

        static void Engine() // Runs the game itself
        {
            string RoomPath = SysVars.path + "Data\\" + SysVars.EngineInfo[0] + "\\" + SysVars.EngineInfo[1] + "\\" + SysVars.EngineInfo[2] + "\\"; //Stores the path to the current room
            string[] OptionText = File.ReadAllLines(RoomPath + "O.txt"); //loops and prints each text with the id of the command
            string[] Links = File.ReadAllLines(RoomPath + "L.txt");  //Reads L.txt
            Console.Clear();

            if (Links.Length != OptionText.Length)//Checks room is valid
            {
                Console.WriteLine("This room is incorectly configured as it doesn't have the same lines in o.txt and l.txt\nIf you are not the developer you should report this,\nthe game will now close as it doesn't know what to do."); //If you are a dev and this happens you should feel bad.
            }

            Console.WriteLine(File.ReadAllText(RoomPath + "T.txt") + "\nOptions:\n"); //This prints all the t.txt file
            for (int i = 1; OptionText.Length >= i; i++)
            {
                Console.WriteLine(i + ")" + OptionText[i - 1]); // Offsets option by one to account for keyboards being 1,9 + 0
            }

            Thread.Sleep(500);
            bool Loop = true; // makes the code below loop until valid input is registered
            int UserSelect;
            while (Loop == true)
            {
                string Select = Console.ReadLine();

                try
                {
                    UserSelect = Convert.ToInt32(Select);
                    if (Links.Length >= UserSelect - 1)
                    {
                        Loop = false;
                    }
                    else
                    {
                        Console.WriteLine("That isn't a valid number");
                    }
                }
                catch 
                {
                    Console.WriteLine("That isn't a number.");
                }
            }

            if (UserSelect == 0)
            {

            }
       
        
        
        }
    }
}
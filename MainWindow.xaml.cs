using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;
using System.Threading;
using System.Net;
using System.IO.Compression;
using System.Diagnostics;

// Looking for line 2?
// Code to be executed by - Line B Refactored Edition
//Its been moved, to see the easteregg go to settings and click on the the licence infomation

namespace NewDawn_Engine
{
    static public class UserData // This stores the variables that are saved between reloads (Exlcudes savedata)
    {
        static public bool AutoUpdate = true;
        public static string Path = AppDomain.CurrentDomain.BaseDirectory; //Gets the executing directory
        public static char SlashType = Path.Last(); //Will get the type of slash (Prevents crashing on Unix Based system as / is used instead of \)
        public static int GameWindowVisibility = 0;
        public static string EngineRoom = ""; //Stores room that the engine should read from
        public static string EngineChapter = ""; //Stores chapter that the engine should read from
        public static string GameDir = "";
        public static List<string> Links = new List<string>(); //Links are the names of folders (ID corresponds with Options)
        public static List<string> Options = new List<string>(); //Options are shown to the user and when selected sends the user to the corresponding link
    }
    partial class MainWindow : Window //This interacts with the UI so bascially this stores buttons and other elements 
    {
        public MainWindow() //This runs at start up and more or less is the closest thing to Main() in console newdawn
        {
            InitializeComponent(); //This initalises the window
            EngineTab.IsEnabled = false;
            string[] GameDirs = Directory.GetDirectories(UserData.Path + UserData.SlashType + "Data");  // This gets the full path to each directory in data
            for (int i = 0; i <= GameDirs.Length - 1; i++)
            {
                GameSelectDropDown.Items.Add(System.IO.Path.GetFileName(GameDirs[i])); //Adds the name of the game folders to the dropdown
            }
        }

        private void EasterEggClick(object sender, RoutedEventArgs e) //Handles Eastergg button (Updated often)
        { //Enjoy the Persona 4 Reference
            MessageBox.Show("Good Evening!\nTonight the heir to the code throne has a big suprise!\nI gonna score myself a UI!\nNot a Dream, Not a hoax!\nRarisma's hunt for a UI.\n\nBut I came prepared!\nI have my Visual Studio Unmentionables.\nThe best of the lot is gonna be all mine!\nWelp here I go!");
        }

        private void AutoUpdateToggleOn(object sender, RoutedEventArgs e) //Ran when checkbox is ticked
        {
            UserData.AutoUpdate = true;
            MessageBox.Show("Auto-Update enabled");
        }

        private void AutoUpdateToggleOff(object sender, RoutedEventArgs e) //Ran when checkbox is ticked
        {
            UserData.AutoUpdate = false;
            MessageBox.Show("Auto-Update disabled");
        }

        public void GameSelectDropDown_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            string[] NFO = File.ReadAllLines(UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + "i.nfo");
            GameMenuInfoBox.Text = NFO[0] + "   \nVersion: " + NFO[3] + "\n\n\nRelease Date: " + NFO[4] + "\n" + NFO[2];
        }

        public void NewGameButton(object sender, RoutedEventArgs e) //Handles Eastergg button (Updated often)
        {
            if (GameSelectDropDown.SelectedIndex != -1) //Checks that combobox isnt blank
            {
                GameMenuInfoBox.Text = "Now Playing - (" + GameSelectDropDown.SelectedValue + ")\n\n Click the game tab to start playing!";
                EngineConfigTab.IsEnabled = false; //Disables config once game has started
                EngineTab.IsEnabled = true; //Enables Engine tab EngineTab
                GameSelectDropDown.IsEnabled = false;
                NewGame.IsEnabled = false;
                UserData.EngineChapter = "1";
                UserData.EngineRoom = "Start";
                UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
                Engine();
            }
            else
            {
                GameMenuInfoBox.Text = "\n\n\n\n	        	        	   	             Hey!\n	     	         You need to Select a game from the box above!"; //Werid spacing to make the text centered in 500x500
            }
        }

        public void Engine() //Yes I fucking compressed the engine class because I cba to fuck with google
        { //Reimplement engine for readability and the full functionality EG variables ect
            UserData.Links.Clear(); //Clears all items in Links
            UserData.Options.Clear();
            EngineText.Text = File.ReadAllText(UserData.GameDir + "T.txt");
            UserData.Options.AddRange(File.ReadAllLines(UserData.GameDir + "O.txt")); //Adds each line in O.txt as a individual item in the list
            UserData.Links.AddRange(File.ReadAllLines(UserData.GameDir + "L.txt")); //Adds each line in O.txt as a individual item in the list

            option0.Content = UserData.Options[0];

            if (UserData.Options.Count > 1)
            {
                option1.IsEnabled = true;
                option1.Opacity = 100;
                option1.Content = UserData.Options[1];
            }
            else
            {
                option1.IsEnabled = false;
                option1.Opacity = 0;
            }
            
            if (UserData.Options.Count > 2)
            {
                option2.IsEnabled = true;
                option2.Opacity = 100;
                option2.Content = UserData.Options[2];
            }
            else
            {
                option2.IsEnabled = false;
                option2.Opacity = 0;
            }

            if (UserData.Options.Count > 3)
            {
                option3.IsEnabled = true;
                option3.Opacity = 100;
                option3.Content = UserData.Options[3];
            }
            else
            {
                option3.IsEnabled = false;
                option3.Opacity = 0;
            }

            if (UserData.Options.Count > 4)
            {
                option4.IsEnabled = true;
                option4.Opacity = 100;
                option4.Content = UserData.Options[4];
            }
            else
            {
                option4.IsEnabled = false;
                option4.Opacity = 0;
            }

            if (UserData.Options.Count > 5)
            {
                option5.IsEnabled = true;
                option5.Opacity = 100;
                option5.Content = UserData.Options[5];
            }
            else
            {
                option5.IsEnabled = false;
                option5.Opacity = 0;
            }

            if (UserData.Options.Count > 6)
            {
                option6.IsEnabled = true;
                option6.Opacity = 100;
                option6.Content = UserData.Options[6];
            }
            else
            {
                option6.IsEnabled = false;
                option6.Opacity = 0;
            }

            if (UserData.Options.Count > 7)
            {
                option7.IsEnabled = true;
                option7.Opacity = 100;
                option7.Content = UserData.Options[7];
            }
            else
            {
                option7.IsEnabled = false;
                option7.Opacity = 0;
            }

            if (UserData.Options.Count > 8)
            {
                option8.IsEnabled = true;
                option8.Opacity = 100;
                option8.Content = UserData.Options[8];
            }
            else
            {
                option8.IsEnabled = false;
                option8.Opacity = 0;
            }

            if (UserData.Options.Count > 9)
            {
                option9.IsEnabled = true;
                option9.Opacity = 100;
                option9.Content = UserData.Options[9];
            }
            else
            {
                option9.IsEnabled = false;
                option9.Opacity = 0;
            }

        }

        public void option0_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[0];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option1_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[1];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option2_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[2];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option3_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[3];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option4_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[4];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option5_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[5];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option6_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[6];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option7_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[7];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option8_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[8];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }

        private void option9_Click(object sender, RoutedEventArgs e)
        {
            UserData.EngineRoom = UserData.Links[9];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.EngineRoom + UserData.SlashType;
            Engine();
        }
    }
}
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Threading;

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
        public static List<string?> TextVar = new List<string?>();  //Text array for engine variable
        public static List<bool?> BoolVar = new List<bool?>(); //Boolean Variable for engine variable
        public static bool Debug = true; //toggles debugblock
        public static List<string?> Saves = new List<string?>(); //Stores the actual name of save folders
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

            if (UserData.Debug == false) //Checks if the game should show the Debugblock (log)
            {
                DebugBlock.IsEnabled = false;
                DebugBlock.Opacity = 0;
            }
            else
            {
                DebugBlock.IsEnabled = true;
                DebugBlock.Opacity = 100;
            }

            SaveCombobox.IsEnabled = false;
            Load.IsEnabled = false;
            DeleteSave.IsEnabled = false;
        }

        private void EasterEggClick(object sender, RoutedEventArgs e) //Handles Eastergg button (Updated often)
        {
            MessageBox.Show("DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA\nDESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA DESTROYA");
        }

        private void AutoUpdateToggle(object sender, RoutedEventArgs e) //Ran when checkbox is clicked
        {

            if (AutoUpdateBox.IsChecked == true)
            {
                UserData.AutoUpdate = true;
                MessageBox.Show("Auto-Update enabled");
            }
            else
            {
                UserData.AutoUpdate = false;
                MessageBox.Show("Auto-Update disabled");
            }
        }

        public void GameSelectDropDown_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            string[] NFO = File.ReadAllLines(UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + "i.nfo");
            GameMenuInfoBox.Text = NFO[0] + "   \nVersion: " + NFO[3] + "\n\n\nRelease Date: " + NFO[4] + "\n" + NFO[2];
            DebugBlock.Text = DebugBlock.Text + "\nSelected game: " + GameSelectDropDown.SelectedValue;
            SaveScan();
        }

        private void SaveScan()
        {
            SaveCombobox.Items.Clear(); //Clears combobox to prevent saves from being shown multiple times

            DebugBlock.Text = DebugBlock.Text + "\nFailed to find save folder";
            SaveCombobox.IsEnabled = false;
            Load.IsEnabled = false;
            DeleteSave.IsEnabled = false;
            SaveInfo.Text = "No saves found";

            UserData.Saves = new List<string?>();
            if (Directory.Exists(UserData.Path + "\\Data\\" + GameSelectDropDown.SelectedValue + "\\Saves"))
            {
                DebugBlock.Text = DebugBlock.Text + "\nFound Saves folder at " + UserData.Path + "\\Data\\" + GameSelectDropDown.SelectedValue + "\\Saves";
                string[] SaveDir = Directory.GetDirectories(UserData.Path + "\\Data\\" + GameSelectDropDown.SelectedValue + "\\Saves");  // This gets the full path to each directory in Saves
                for (int i = 0; i <= SaveDir.Length - 1; i++)
                {
                    SaveCombobox.Items.Add(DateTimeOffset.FromUnixTimeSeconds(Convert.ToInt32(Path.GetFileName(SaveDir[i])))); //Gets the name of the folder (Which is saved in Unix Second format) and converts it to a real time and then adds this to the dropdown
                    UserData.Saves.Add(Path.GetFileName(SaveDir[i]));
                }
                if (SaveDir.Count() - 1 >= 0)
                {
                    DebugBlock.Text = DebugBlock.Text + "\nAmmount of saves - " + SaveCombobox.Items.Count;
                    SaveCombobox.IsEnabled = true;
                    Load.IsEnabled = true;
                    DeleteSave.IsEnabled = true;
                    SaveInfo.Text = "Select a save to load";
                }
            }
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
                Load.IsEnabled = false;
                SaveCombobox.IsEnabled = false;
                DeleteSave.IsEnabled = false;
                UserData.EngineChapter = "1";
                UserData.EngineRoom = "Start";
                UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + "1" + UserData.SlashType + "Start" + UserData.SlashType;

                for (int I = 0; I < 10000; I++) //Nulls 10K elements to prevent them from being read as false 
                {
                    UserData.BoolVar.Add(null);
                    UserData.TextVar.Add(null);
                }

                if (UserData.Debug == false) //Checks if the game should show the Debugblock (log)
                {
                    DebugBlock.IsEnabled = false;
                    DebugBlock.Opacity = 0;
                }
                else
                {
                    DebugBlock.IsEnabled = true;
                    DebugBlock.Opacity = 100;
                }

                EngineInitalise();
            }
            else
            {
                GameMenuInfoBox.Text = "\n\n\n\n	        	        	   	             Hey!\n	     	         You need to Select a game from the box above!"; //Werid spacing to make the text centered in 500x500
            }
        }

        public void EngineInitalise()
        {
            if (File.Exists(UserData.GameDir + "ChapterChange.txt") == true) // Checks if a chapter Change exists
            {
                string[] Temp = File.ReadAllLines(UserData.GameDir + "ChapterChange.txt");
                UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + Temp[0] + UserData.SlashType + "Start" + UserData.SlashType;
                UserData.EngineChapter = Temp[0];
                EngineInitalise();
            }

            UserData.Links.Clear(); //Clears all items in Links
            UserData.Options.Clear();
            EngineText.Text = File.ReadAllText(UserData.GameDir + "T.txt");
            DebugBlock.Text = DebugBlock.Text + "\nInitalised room at " + UserData.GameDir;


            UserData.Options.AddRange(File.ReadAllLines(UserData.GameDir + "O.txt")); //Adds each line in O.txt as a individual item in the list
            UserData.Links.AddRange(File.ReadAllLines(UserData.GameDir + "L.txt")); //Adds each line in O.txt as a individual item in the list
            option0.Content = UserData.Options[0]; //Since there will always be atleast 1 options 0 will always be used
            DebugBlock.Text = DebugBlock.Text + "\nLoaded Options and Links";
            EngineVariable();
        }

        public void EngineVariable()
        {
            DebugBlock.Text = DebugBlock.Text + "\nIs VarSet.text present - " + File.Exists(UserData.GameDir + "VarSet.txt") ;
            DebugBlock.Text = DebugBlock.Text + "\nIs VarCheck.txt Present - " + File.Exists(UserData.GameDir + "VarCheck.txt");
            string[] TempFile; //Used as a temporary file reader
            if (File.Exists(UserData.GameDir + "VarSet.txt")) // This Sets Variables
            {
                TempFile = File.ReadAllLines(UserData.GameDir + "VarSet.txt"); // (0 - bool/text  1 - Place in array   2 - Value)
                if (TempFile[0] == "bool")
                {
                    if (TempFile[2] == "false")
                    {
                        UserData.BoolVar[Convert.ToInt32(TempFile[1])] = false;
                        DebugBlock.Text = DebugBlock.Text + "\nSet boolean variable " + TempFile[1] + " to " + TempFile[2];
                    }
                    else if (TempFile[2] == "true")
                    {
                        UserData.BoolVar[Convert.ToInt32(TempFile[1])] = true;
                        DebugBlock.Text = DebugBlock.Text + "\nSet boolean variable " + TempFile[1] + " to " + TempFile[2];
                    }
                }
                else if (TempFile[0] == "text")
                {
                    UserData.TextVar[Convert.ToInt32(TempFile[1])] = TempFile[2];
                    DebugBlock.Text = DebugBlock.Text + "\nSet string variable " + TempFile[1] + " to " + TempFile[2];
                }
            }

            if (File.Exists(UserData.GameDir + "VarCheck.txt"))// Checks Variables
            {//0-text/bool 1-Position in array 2-expected result 3-Positive Result Option 4- Positive result link
                TempFile = File.ReadAllLines(UserData.GameDir + "VarCheck.txt");
                DebugBlock.Text = DebugBlock.Text + "\nFound a VarCheck File";
                if (TempFile[0] == "bool")
                {
                    DebugBlock.Text = DebugBlock.Text + "\nChecking a bool variable";
                    DebugBlock.Text = DebugBlock.Text + "\nChecking " + TempFile[2] + "==" + Convert.ToString(UserData.BoolVar[Convert.ToInt32(TempFile[1])]);

                    if (TempFile[2].ToUpper() == Convert.ToString(UserData.BoolVar[Convert.ToInt32(TempFile[1])]).ToUpper()) //Converts sp
                    {
                        DebugBlock.Text = DebugBlock.Text + "\nBool Variable matches requirement";

                        UserData.Options.Add(TempFile[3]);
                        UserData.Links.Add(TempFile[4]);
                    }
                    else
                    {
                        DebugBlock.Text = DebugBlock.Text + "\nBool Variable DOES NOT requirement";
                    }
                    DebugBlock.Text = DebugBlock.Text + System.Convert.ToString("\nChecking boolean variable " + TempFile[1] + " - Expected:" + TempFile[2] + " Reality:" + TempFile[2] == Convert.ToString(UserData.BoolVar[Convert.ToInt32(TempFile[1])]));
                }
                else if (TempFile[0] == "text")
                {
                    if (TempFile[2].ToUpper() == Convert.ToString(UserData.TextVar[Convert.ToInt32(TempFile[1])]).ToUpper()) //Converts sp
                    {
                        UserData.Options.Add(TempFile[3]);
                        UserData.Links.Add(TempFile[4]);
                    }
                    DebugBlock.Text = DebugBlock.Text + System.Convert.ToString("\nChecking string variable " + TempFile[1] + " - Expected: " + TempFile[2] + " Reality:" + TempFile[2] == Convert.ToString(UserData.TextVar[Convert.ToInt32(TempFile[1])]));
                }
                else
                {
                    Thread.Sleep(0);
                    DebugBlock.Text = DebugBlock.Text + "Failed to find a VarCheck File";
                }
            }
            EngineButtonHandler();
        }

        public void EngineButtonHandler() // Just for readability I confined all the buttony stuff into a single function
        {
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

        void optionclick(object sender, RoutedEventArgs e)
        {
            Button button = sender as Button;
            string ButtonNumber = Convert.ToString(button.Name.Replace("option", ""));
            DebugBlock.Text = DebugBlock.Text + "\nParsed ButtonNumber to " + ButtonNumber + "\nSending player to " + UserData.Links[Convert.ToInt32(ButtonNumber)] + "\n\n\n\n";
            UserData.EngineRoom = UserData.Links[Convert.ToInt32(ButtonNumber)];
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + UserData.EngineChapter + UserData.SlashType + UserData.Links[Convert.ToInt32(ButtonNumber)] + UserData.SlashType; EngineInitalise();
            EngineInitalise();
        }

        public void SaveGame(object sender, RoutedEventArgs e)
        {
            string SaveDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + "\\Saves\\" + Convert.ToString(DateTimeOffset.Now.ToUnixTimeSeconds());

            List<string?> SaveTextVar = new List<string?>();
            List<string?> SaveBoolVar = new List<string?>();
            for (int i = 0; i <= UserData.BoolVar.Count - 1; i++)
            {

                if (UserData.TextVar[i] == null)
                {
                    SaveTextVar.Add("null");
                }
                else
                {
                    SaveTextVar.Add(UserData.TextVar[i]);
                }

                if (UserData.BoolVar[i] == null)
                {
                    SaveBoolVar.Add("null");
                }
                else
                {
                    SaveBoolVar.Add(Convert.ToString(UserData.BoolVar[i]));
                }
            }

            string[] temp = { UserData.EngineChapter, UserData.EngineRoom };
            Directory.CreateDirectory(SaveDir);
            File.WriteAllLines(SaveDir + "\\TextVar", SaveTextVar);
            File.WriteAllLines(SaveDir + "\\BoolVar", SaveBoolVar);
            File.WriteAllLines(SaveDir + "\\UserData", temp);
        }//Its like LoadGame() but in reverse

        private void LoadGame(object sender, RoutedEventArgs e) //Its like SaveGame() but in reverse
        {
            string SaveDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + "\\Saves\\" + UserData.Saves[SaveCombobox.SelectedIndex];

            UserData.TextVar = new List<string?>();
            UserData.BoolVar = new List<bool?>();
            string[] ReadTextVar = File.ReadAllLines(SaveDir + "\\TextVar");
            string[] ReadBoolVar = File.ReadAllLines(SaveDir + "\\BoolVar");
            string[] ReadRoomDat = File.ReadAllLines(SaveDir + "\\UserData");
            SaveInfo.Text = "Loading...";

            for (int i = 0; i <= ReadTextVar.Count() - 1; i++){

                if (ReadTextVar[i] == "null")
                {
                    UserData.TextVar.Add(null);
                }
                else
                {
                    UserData.TextVar.Add(ReadTextVar[i]);
                }

                if (ReadBoolVar[i] == null)
                {
                    UserData.BoolVar.Add(null);
                }
                else
                {
                    if (ReadBoolVar[i] == "false")
                    {
                        UserData.BoolVar.Add(false);
                    }
                    else
                    {
                        UserData.BoolVar.Add(true);
                    }
                }
            }
            DebugBlock.Text = DebugBlock.Text + "\n\nAdded " + UserData.BoolVar.Count + " to Boolean Variable\n\nAdded " + UserData.TextVar.Count + " to TextVariable";
            UserData.GameDir = UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + ReadRoomDat[0] + UserData.SlashType + ReadRoomDat[1] + UserData.SlashType;
            GameMenuInfoBox.Text = "Now Playing - (" + GameSelectDropDown.SelectedValue + ")\n\n Click the game tab to start playing!";
            EngineConfigTab.IsEnabled = false; //Disables config once game has started
            EngineTab.IsEnabled = true; //Enables Engine tab EngineTab
            GameSelectDropDown.IsEnabled = false;
            NewGame.IsEnabled = false;
            Load.IsEnabled = false;
            SaveCombobox.IsEnabled = false;
            DeleteSave.IsEnabled = false;
            SaveInfo.Text = "Loaded!";
            EngineInitalise();
        }

        private void DeleteSave_Click(object sender, RoutedEventArgs e)
        {
            Directory.Delete(UserData.Path + "data" + UserData.SlashType + GameSelectDropDown.SelectedValue + UserData.SlashType + "\\Saves\\" + UserData.Saves[SaveCombobox.SelectedIndex], true);
            SaveScan();
        }
    }
}
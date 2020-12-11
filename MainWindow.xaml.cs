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

namespace NewDawn_GUI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    static public class UserData // This stores the variables that are saved between reloads (Exlcudes savedata)
    {
       static public bool AutoUpdate = true;
    }
     partial class MainWindow : Window //This stores the main menu
     {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void EasterEggClick(object sender, RoutedEventArgs e) //Handles Eastergg button (Updated often)
        {
            MessageBox.Show("Tomorrow comes Today Edition!");
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
    }
}

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
using System.Windows.Shapes;
using System.IO;

namespace Games_Prices
{
    /// <summary>
    /// Logika interakcji dla klasy NewGameWindow.xaml
    /// </summary>
    public partial class NewGameWindow : Window
    {
        public NewGameWindow()
        {
            InitializeComponent();
        }

        private void Grid_MouseDown(object sender, MouseButtonEventArgs e)
        {
            try
            {
                DragMove();
            }
            catch
            {

            }
        }

        //Saving Data

        bool SaveToTxt()
        {
            using (StreamWriter sw = new StreamWriter("games.txt", true))
            {
                sw.WriteLine("{0}|{1}", linkTxt.Text, platformCmb.Text);
                sw.Close();
            }
            return true;
        }

        //Buttons

        private void saveBtn_Click(object sender, RoutedEventArgs e)
        {
            SaveToTxt();
            this.Close();
        }

        private void cancelBtn_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        //Textboxes

        private void linkTxt_GotFocus(object sender, RoutedEventArgs e)
        {
            linkTxt.Text = "";
        }
    }
}

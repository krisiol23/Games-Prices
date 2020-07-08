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

namespace Games_Prices
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private List<Game> GamesList;

        public MainWindow()
        {
            InitializeComponent();

            GamesList = new List<Game>();
        }

        private void StackPanel_MouseDown(object sender, MouseButtonEventArgs e)
        {
            try
            {
                DragMove();
            }
            catch
            {

            }
        }

        //Reading Data
        private void ReadData()
        {
            GamesList.Clear();

            using (StreamReader sr = new StreamReader("games.txt"))
            {
                string line;

                while ((line = sr.ReadLine()) != null)
                {
                    string[] par = line.Split('|');

                    Game game = new Game(par[0], par[1], par[2], par[3]);

                    if (!GamesList.Contains(game))
                    {
                        GamesList.Add(game);
                    }
                }
            }
        }

        //Buttons 

        private void exitBtn_Click(object sender, RoutedEventArgs e)
            {
                this.Close();
            }

            private void minimizeBtn_Click(object sender, RoutedEventArgs e)
            {
                this.WindowState = WindowState.Minimized;
            }

            private void addGameBtn_Click(object sender, RoutedEventArgs e)
            {
                NewGameWindow ngw = new NewGameWindow();
                ngw.Show();
            }

            private void delGameBtn_Click(object sender, RoutedEventArgs e)
            {

            }
        
    }
}

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
using System.Diagnostics;
using System.Windows.Documents.Serialization;
using System.Windows.Media.Animation;

namespace Games_Prices
{
    public partial class MainWindow : Window
    {
        private List<Game> GamesList;

        public MainWindow()
        {
            InitializeComponent();

            GamesList = new List<Game>();
            readData();

            gamesBox.ItemsSource = null;
            gamesBox.ItemsSource = GamesList;
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

        private void readData()
        {
            GamesList.Clear();

            using (StreamReader sr = new StreamReader("data.txt"))
            {
                string line;

                while ((line = sr.ReadLine()) != null)
                {
                    string[] par = line.Split('|');

                    string actualPrice = execCheckProcess(par[2], par[1]);
                    actualPrice = formatPrice(actualPrice);
                    string price = formatPrice(par[3]);
                    char compareChar = comparePrices(double.Parse(price), double.Parse(actualPrice));

                    Game game = new Game(par[0], par[1], par[2], par[3], actualPrice, compareChar);

                    if (!GamesList.Contains(game))
                    {
                        GamesList.Add(game);
                    }
                }
            }
        }

        private void deleteGame(Game game)
        {
            GamesList.Remove(game);

            using (FileStream fs = new FileStream("data.txt", FileMode.Truncate))
            { }

            using (StreamWriter sw = new StreamWriter("data.txt", true))
            {
                foreach (Game g in GamesList)
                {
                    sw.WriteLine("{0}|{1}|{2}|{3}", g.title, g.platform, g.url, g.price);
                }
            }
        }

        char comparePrices(double price, double actualPrice)
        {
            char arrow;
            if(actualPrice == price)
            {
                arrow = '-';
            }
            else if(actualPrice < price)
            {
                arrow = '↓';
            }
            else
            {
                arrow = '↑';
            }
            return arrow;
        }
        string formatPrice(string price)
        {
            price = price.Replace("zl", String.Empty);
            price = price.Replace("zł", String.Empty);
            price = price.Replace(" ", String.Empty);
            return price;
        }

        //Python Connection

        static string execCheckProcess(string gameUrl, string gamePlatform)
        {
            var psi = new ProcessStartInfo();
            psi.FileName = @"D:\Program Files (x86)\python.exe";

            var script = @"check.py";
            var url = gameUrl;
            var value = gamePlatform;

            psi.Arguments = $"\"{script}\" \"{url}\" \"{value}\"";

            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;

            var results = "";

            using (var process = Process.Start(psi))
            {
                results = process.StandardOutput.ReadToEnd();
            }
            return results;
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
                NewGameWindow newg = new NewGameWindow();
                newg.showForm();
            }

            private void delGameBtn_Click(object sender, RoutedEventArgs e)
            {
                deleteGame(gamesBox.SelectedItem as Game);
                gamesBox.ItemsSource = null;
                gamesBox.ItemsSource = GamesList;
        }

        private void helpBtn_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Symbols: '-' if price is the same. '↓' if price is lower. '↑' if price is higher than last one.");
        }

        private void refreshBtn_Click(object sender, RoutedEventArgs e)
        {
            readData();

            gamesBox.ItemsSource = null;
            gamesBox.ItemsSource = GamesList;
        }
    }
}

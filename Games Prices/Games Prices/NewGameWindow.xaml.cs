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
using System.Diagnostics;

namespace Games_Prices
{
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

        //Python Connection

        static string execProcess(string link, string platform)
        {
            var psi = new ProcessStartInfo();
            psi.FileName = @"D:\Program Files (x86)\python.exe";

            var script = @"script.py";
            var url = link;
            var value = platform;

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
        public void showForm()
        {
            this.Show();
        }

        //Buttons

        private void saveBtn_Click(object sender, RoutedEventArgs e)
        {
            execProcess(linkTxt.Text, platformCmb.Text);
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

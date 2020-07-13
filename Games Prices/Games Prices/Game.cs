using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;

namespace Games_Prices
{
    public class Game
    {
        public string title { get; set; }
        public string platform { get; set; }
        public string url { get; set; }
        public string price { get; set; }
        public string actualPrice { get; set; }
        public char compareChar { get; set; }

        public Game(string t, string p, string u, string pr, string ap, char c)
            {
            title = t;
            platform = p;
            url = u;
            price = pr;
            actualPrice = ap;
            compareChar = c;
            }

        public override string ToString()
        {
            return title + " on " + platform + " " + actualPrice + " " + compareChar;
        }
    }
}

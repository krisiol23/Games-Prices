using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Games_Prices
{
    public class Game
    {
        private string title { get; set; }
        private string platform { get; set; }
        private string price { get; set; }
        private string actualPrice { get; set; }

        public Game(string t, string p, string pr, string ap)
            {
            title = t;
            platform = p;
            pr = price;
            actualPrice = ap;
            }

        public override string ToString()
        {
            return title + " " + platform + " " + actualPrice;
        }
    }
}

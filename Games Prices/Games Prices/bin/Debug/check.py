import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

game_url = sys.argv[1]
platform = sys.argv[2]

price = ""

def get_url(game_url, platform):

        if(platform == "Steam"):
                print(steamScrap(game_url, platform))


        elif(platform == "Uplay"):
                print(uplayScrap(game_url, platform))

def steamScrap(game_url, value):
        table = []

        uClient = uReq(game_url)
        page_html = uClient.read()
        uClient.close() 

        page_soup = soup(page_html, "html.parser") 

        x = page_soup.findAll("div", {"class":"discount_pct"})

        if not x:
                game_price1 = page_soup.findAll("div", {"class":"game_purchase_price price"})
                for p in game_price1:
                        game_price1 = p.text
                        game_price1 = game_price1.strip()
                        table.append(game_price1)
                
                actual_price = table[0]


        elif(x == x):
                game_price1 = page_soup.findAll("div", {"class":"discount_final_price"})
                for p in game_price1:
                        game_price1 = p.text
                        game_price1 = game_price1.strip()
                        table.append(game_price1)
                
                actual_price = table[0]
        return actual_price

def uplayScrap(game_url, value):
        table = []

        uClient = uReq(game_url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        game_name = page_soup.findAll("div", {"class":"product-title-wrapper"})
        game_price = page_soup.findAll("span", {"class":"price-sales standard-price"})

        for p in game_price:
                game_price = p.text
                game_price = game_price.strip()
                table.append(game_price)

        table = table[12:]
        table = table[0]
        game_price = table
        game_price = game_price.split()
        game_currency = game_price[0]
        game_value = game_price[1]

        x = game_value, game_currency

        string = ""
        for j in x:
                string += j

        x = string

        actual_price = x
        return actual_price
    
get_url(game_url, platform)
    



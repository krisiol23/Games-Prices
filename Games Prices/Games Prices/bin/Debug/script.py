import sys
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

game_url = sys.argv[1]
value = sys.argv[2]

def get_url(game_url, value):

        if(value == "Steam"):
                steamScrap(game_url, value)
                saveLinkToFile(game_url)

        elif(value == "Uplay"):
                uplayScrap(game_url, value)
                saveLinkToFile(game_url)

def steamScrap(game_url, value):
        table = []

        uClient = uReq(game_url)
        page_html = uClient.read()
        uClient.close() 

        page_soup = soup(page_html, "html.parser") 

        game_name = page_soup.findAll("div", {"class":"apphub_AppName"}) 
    
        
        for p in game_name: 
                game_name = p.text

        x = page_soup.findAll("div", {"class":"discount_pct"})

        if not x:
                game_price1 = page_soup.findAll("div", {"class":"game_purchase_price price"})
                for p in game_price1:
                        game_price1 = p.text
                        game_price1 = game_price1.strip()
                        game_price1 = game_price1.replace("zł", "zl")
                        table.append(game_price1)
                
                game_price1 = table[0]
                ready = game_name + "|" + value + "|"+ game_url + "|" + table[0]
                saveToFile(ready)

        elif(x == x):
                game_price1 = page_soup.findAll("div", {"class":"discount_final_price"})
                for p in game_price1:
                        game_price1 = p.text
                        game_price1 = game_price1.strip()
                        game_price1 = game_price1.replace("zł", "zl")
                        table.append(game_price1)
                
                game_price1 = table[0]

                ready = game_name + "|" + value + "|"+ game_url + "|" + table[0]
                print(ready)
                saveToFile(ready)

def uplayScrap(game_url, value):
        table = []

        uClient = uReq(game_url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        game_name = page_soup.findAll("div", {"class":"product-title-wrapper"})
        game_price = page_soup.findAll("span", {"class":"price-sales standard-price"})

        for p in game_name:
                game_name = p.text
                game_name = game_name.strip()

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

        ready = game_name + "|" + value + "|" + game_url + "|" + x

        saveToFile(ready)


def saveToFile(toSave):
        txt_file = open("data.txt" , "a")
        txt_file.write(" " +toSave+"\n")
        txt_file.close()

get_url(game_url, value)

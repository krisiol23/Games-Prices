#libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


game_url= input()

uClient = uReq(game_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

game_name = page_soup.findAll("div", {"class":"apphub_AppName"})
game_price = page_soup.findAll("div", {"class":"game_purchase_price price"})

for p in game_name:
     game_name = p.text

for p in game_price:
    game_price = p.text
    game_price = game_price.strip()


print(game_name)
print(game_price)

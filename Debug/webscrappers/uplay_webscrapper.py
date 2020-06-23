from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq 

table = []

game_url= input("uplay game link: ")

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

game_price = game_price.split()
game_currency = game_price[0]
game_value = game_price[1]

x = game_value, game_currency

string = ""
for j in x:
	string += j

x = string 
#print(x)
print(game_name) 
print(game_value,game_currency)


ready = game_name + " " + value + " " + x 

txt_file = open("data.txt" , "a") 
txt_file.write(ready+"\n") 
txt_file.close() 



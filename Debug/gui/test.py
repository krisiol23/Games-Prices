from bs4 import BeautifulSoup as soup #biblioteka do pobierania danych ze strony
from urllib.request import urlopen as uReq #biblitoeka do nawiązywania połączenia ze stronką

table = []
table1 = []
table2 = []
actual_prices = []

# url = "https://store.steampowered.com/app/969990/SpongeBob_SquarePants_Battle_for_Bikini_Bottom__Rehydrated/"
url = "https://store.steampowered.com/app/105600/Terraria/"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
game_price = page_soup.findAll("div", {"class":"game_purchase_price price"})
try:
	cycki = page_soup.findAll("div", {"class":"discount_final_price"})
	cycki = cycki[0]
except:
	pass
print(game_price)
print(cycki)


if(game_price[0] == game_price[0]):
	if not(cycki == cycki):	
		print("dzała")
		game_price2 = page_soup.findAll("div", {"class":"discount_final_price"})
		print(game_price2)
		for p in game_price2:
			game_price2 = p.text
			game_price2 = game_price2.strip()
			table2.append(game_price2)
		game_price2 = table2[0]
		actual_prices.append(game_price2)	
else:
	print("koniec")
if not game_price:
	game_price1 = page_soup.findAll("div", {"class":"discount_final_price"})
	for p in game_price1:
		game_price1 = p.text
		game_price1 = game_price1.strip()
		table1.append(game_price1)
	
	game_price1 = table1[0]
	#print(game_price)
	actual_prices.append(game_price1)

else:
	for p in game_price:
		game_price = p.text
		game_price = game_price.strip()
		table.append(game_price)

	game_price = table[0]
	#print(game_price)
	actual_prices.append(game_price)
	print(actual_prices)
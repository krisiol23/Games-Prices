#!/usr/bin/python3
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json
import requests
print ("dupa")



game_url= input("wpisz nazwe gry: ")
game_url = game_url.replace(" ","-")
game_url = game_url.lower()


page_url="https://www.epicgames.com/store/en-US/product/" + game_url

print (page_url)

uClient = uReq(page_url)

page_html = uClient.read()

uClient.close()


page_soup = soup(page_html, "html.parser")

game_name = page_soup.findAll("h1", {"class":"Markdown-heading_4f36fd81"})
print (game_name)

game_price = page_soup.findAll("div", {"class":"PurchasePrice-priceContainer_f0baeac9"})
print (game_price.span)

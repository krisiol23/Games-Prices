#!/usr/bin/python3
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
from urllib.request import urlopen as uReq
print ("dupa")


#game_url = input("Origin game link: ")
game_url = 'https://www.origin.com/pol/en-us/store/battlefield/battlefield-v/'

print("elo")

#source = requests.get(game_url).text
#page_soup = soup(source, 'lxml')


game_name = game_url
game_name = game_url.replace(game_url[0:39],"")
game_name = game_name.replace("/"," ")
#print (game_name)
game_name = game_name.split()
#print (game_name)
g4me_name = game_name[1].capitalize()
print(g4me_name)

game_price = game_url + "interstitial"

uClient = uReq(game_price)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


game_price = page_soup.findAll("div", {"class":"otkex-priceblock-pricewrapper"})
print(game_price)




#[d for d in soup.findAll('div') if not d.find('div')]

#driver = webdriver.PhantomJS(executable_path='/home/malpa/Pobrane/phantomjs-2.1.1-linux-x86_64/bin/')
#driver.get(game_url)
print(2222)
#bsObj = soup(driver.page_source,'html.parser')
#p_element = driver.find_element_byclassname('otkex-product-hero-leftrail-text')
#print(p_element.text)



#game_price = page_soup.findAll("div", {"class":"game_purchase_price price"})


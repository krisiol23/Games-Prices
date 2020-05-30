#!/usr/bin/python3
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
print ("dupa")


#game_url = input("Origin game link: ")
game_url = 'https://www.origin.com/pol/en-us/store/fifa/fifa-20'

print("elo")

#source = requests.get(game_url).text
#page_soup = soup(source, 'lxml')


#[d for d in soup.findAll('div') if not d.find('div')]

driver = webdriver.PhantomJS(executable_path='/home/malpa/Pobrane/phantomjs-2.1.1-linux-x86_64/bin/')
driver.get(game_url)
print(2222)
bsObj = soup(driver.page_source,'html.parser')
p_element = driver.find_element_byclassname('otkex-product-hero-leftrail-text')
#print(p_element.text)



game_price = page_soup.findAll("div", {"class":"game_purchase_price price"})


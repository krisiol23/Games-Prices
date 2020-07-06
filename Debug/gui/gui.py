#!/usr/bin/python3
import tkinter
from tkinter import *
from tkinter import ttk
import os
#biblioteki
from bs4 import BeautifulSoup as soup #biblioteka do pobierania danych ze strony
from urllib.request import urlopen as uReq #biblitoeka do nawiązywania połączenia ze stronką
import time

window = tkinter.Tk()
window.title("Games_prices")

actual_prices = []
file_prices = []

def clear():
	open("data.txt", "w").close()
	open("links.txt", "w").close()

def get_url():
	game_url = textbox.get()
	textbox.delete(0, END)
	value = combobox.get()

	if(value == "Steam"):
		steamScrap(game_url, value)
		saveLinkToFile(game_url)

	elif(value == "Epic Games"):
		wrong_label = Label(window, text = "Coming soon!", fg = "black")
		wrong_label.grid(row = 4, column = 0)
		window.after(2000, wrong_label.destroy)

	elif(value == "Origin"):
		wrong_label = Label(window, text = "Coming soon!", fg = "black")
		wrong_label.grid(row = 4, column = 0)
		window.after(2000, wrong_label.destroy)

	elif(value == "Uplay"):
		uplayScrap(game_url, value)
		saveLinkToFile(game_url)

	else:
		wrong_label = Label(window, text = "ERROR", fg = "red")
		wrong_label.grid(row = 4, column = 0)
		window.after(2000, wrong_label.destroy)


	
label = Label(window, text = "Game link")
label.grid(row = 0, column = 0)

textbox = Entry(window)
textbox.grid(row = 1, column = 0, padx = 5, pady = 10)
button = Button(window, text="ADD", bg = "pink", command = get_url)
button.grid(row = 1, column  = 1)

combobox = ttk.Combobox(window, values = ["Epic Games", "Steam", "Origin", "Uplay"], state = "readonly", width = 17)
combobox.grid(row = 2, column = 0)


button1 = Button(window, text="CLEAR", command = clear)
button1.grid(row = 3, column = 0, pady = 10)

#path = os.getcwd()
#parent = os.path.dirname(path)
#new = os.chdir("../webscrappers")

def saveToFile(toSave):
	txt_file = open("data.txt" , "a") #otwieramy plik data.txt z uprawnieniami read + write
	txt_file.write(" " +toSave+"\n") #zapisujemy w naszym txt stringa którego utworzylismy powyżej
	txt_file.close() #zapisujemy plik

def getTitles():
	test = []
	j = 4
	with open("data.txt") as f:
		cos = f.readlines()

		for x in cos:
			x = x[:-1]
			test.append(x)

		for line in test:
			label = Label(window, text = line)
			label.grid(row = j, column = 2)

			j+=1
			

def steamScrap(game_url, value):
	table = []

	uClient = uReq(game_url) #nawiązujemy połączenie ze stronką pod linkiem który znajduje się w zmiennej game_url
	page_html = uClient.read() #zapisujemy do zmiennej page_html kod html tej strony do której się połączyliśmy
	uClient.close() #jak mamy juz kod html z którego korzystać będzie biblioteka bs4 to zamykamy połączenie ze stroną

	page_soup = soup(page_html, "html.parser") #parsujemy kod html do zmiennej page_soup

	game_name = page_soup.findAll("div", {"class":"apphub_AppName"}) #zapisujemy do zmiennej game_name linijke html który zawiera div z klasą "apphub_AppName"
	game_price = page_soup.findAll("div", {"class":"game_purchase_price price"}) #to samo działanie co powyżej
	
	for p in game_name: #ta pętla służy do wyciągnięcia z tej linijki html kawałka tekstu który nas interesuje
		game_name = p.text

	if not game_price:
		game_price1 = page_soup.findAll("div", {"class":"discount_final_price"})
		for p in game_price1:
			game_price1 = p.text
			game_price1 = game_price1.strip()
			table.append(game_price1)

		ready = game_name + " " + value + " " + table[0] #robimy stringa z wynikami naszego wyszukiwania
		saveToFile(ready)
		getTitles()
	
	else:
		for p in game_price:#to samo co poœyższa petla
			game_price = p.text
			game_price = game_price.strip() #jeżeli nawali nam niepotrzebnych spacji w stringu w którym mamy nasz tekst to używamy na nim maetody stripe() aby się ich pozbyć
			table.append(game_price)


		ready = game_name + " " + value + " " + table[0] #robimy stringa z wynikami naszego wyszukiwania
		saveToFile(ready)
		getTitles()

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
	#print(x)
	# print(game_name)
	# print(game_value,game_currency)

	ready = game_name + " " + value + " " + x

	saveToFile(ready)
	getTitles()

def steamCheck(url):
	table = []
	table1 = []
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html, "html.parser")
	game_price = page_soup.findAll("div", {"class":"game_purchase_price price"})
	
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

def uplayCheck(url):
	table = []
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html, "html.parser")
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

	actual_prices.append(x)

def saveLinkToFile(game_link):
	link_file = open("links.txt" , "a") #otwieramy plik data.txt z uprawnieniami read + write
	link_file.write(" " + game_link+"\n") #zapisujemy w naszym txt stringa którego utworzylismy powyżej
	link_file.close() #zapisujemy plik


def checkPrices():
	global actual_prices
	global file_prices
	testb = []
	testa = []

	prices = []
	links = []
	with open("data.txt") as f:
		price = f.read()
		prices += price.split(" ")
		del prices[0]
	with open("links.txt") as f:
		link = f.read()
		links += link.split(" ")
		del links[0]
	#print(prices)
	#print(links)

	for x in prices:
		if(len(x) >= 6):
			if(x[-6] == ","):
				file_prices.append(x)



	for x in links:
		if(x[8:26] == "store.steampowered"):
			steamCheck(x)
		elif(x[8:17] == "store.ubi"):
			uplayCheck(x)

	print(actual_prices)
	print(file_prices)


	for x in actual_prices:
		x = x[:-2]
		x = x.replace(",", ".")
		testa.append(x)

	for x in file_prices:
		x = x[:-3]
		x = x.replace(",", ".")
		testb.append(x)

		up = "Price increased ↑"
		down = "Price decreased ↓"
		same = "Price is same ↔"

	for i in range(len(file_prices)):
		j = 4
		if(float(testa[i]) < float(testb[i])):
			up = Label(window, text = "↑")
			up.grid(row = j, column = 3)
			print("up")
			j += 1
		if(float(testa[i]) == float(testb[i])):
			same = Label(window, text = "↔")
			same.grid(row = j, column = 3)
			j+=1 
			print("same")

		elif(float(testa[i]) > float(testb[i])):
			print("down")
			down = Label(window, text = "↓")
			down.grid(row = j, column = 3)
			j+=1
		

checkPrices()

getTitles()



window.geometry("500x400")
window.mainloop()

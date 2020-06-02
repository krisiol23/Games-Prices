#!/usr/bin/python3
import tkinter
from tkinter import *
from tkinter import ttk
import os
#biblioteki
from bs4 import BeautifulSoup as soup #biblioteka do pobierania danych ze strony
from urllib.request import urlopen as uReq #biblitoeka do nawiązywania połączenia ze stronką

window = tkinter. Tk()
window.title("Games_prices")

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

	elif(value == "Origin"):
		wrong_label = Label(window, text = "Coming soon!", fg = "black")
		wrong_label.grid(row = 4, column = 0)

	elif(value == "Uplay"):
		print("wdasda")
		saveLinkToFile(game_url)

	else:
		wrong_label = Label(window, text = "ERROR", fg = "red")
		wrong_label.grid(row = 4, column = 0)


label = Label(window, text = "Game link")
label.grid(row = 0, column = 0)

textbox = Entry(window)
textbox.grid(row = 1, column = 0, padx = 5, pady = 10)
button = Button(window, text="ADD", bg = "pink", command = get_url)
button.grid(row = 1, column  = 1)

combobox = ttk.Combobox(window, values = ["Epic Games", "Steam", "Origin", "Uplay"], state = "readonly", width = 17)
combobox.grid(row = 2, column = 0)


button1 = Button(window, text="REFRESH", command = clear)
button1.grid(row = 3, column = 0, pady = 10)

#path = os.getcwd()
#parent = os.path.dirname(path)
#new = os.chdir("../webscrappers")

def saveToFile(toSave):
	txt_file = open("data.txt" , "a") #otwieramy plik data.txt z uprawnieniami read + write
	txt_file.write(" " +toSave+"\n") #zapisujemy w naszym txt stringa którego utworzylismy powyżej
	txt_file.close() #zapisujemy plik

def getTitles():
	with open("data.txt") as f:
		label1 = Label(window, text = f.read())
		label1.grid(row = 4, column = 2)

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


	for p in game_price:#to samo co poœyższa petla
		game_price = p.text
		game_price = game_price.strip() #jeżeli nawali nam niepotrzebnych spacji w stringu w którym mamy nasz tekst to używamy na nim maetody stripe() aby się ich pozbyć
		table.append(game_price)

	ready = game_name + " " + value + " " + table[0] #robimy stringa z wynikami naszego wyszukiwania
	saveToFile(ready)
	getTitles()
	checkPrices()

def saveLinkToFile(game_link):
	link_file = open("links.txt" , "a") #otwieramy plik data.txt z uprawnieniami read + write
	link_file.write(" " + game_link+"\n") #zapisujemy w naszym txt stringa którego utworzylismy powyżej
	link_file.close() #zapisujemy plik

def checkPrices():
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
	print(prices)
	print(links)

checkPrices()

getTitles()


window.geometry("400x400")
window.mainloop()

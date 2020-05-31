#!/usr/bin/python3
import tkinter
from tkinter import *
from tkinter import ttk
import os
from bs4 import BeautifulSoup as soup #biblioteka do pobierania danych ze strony
from urllib.request import urlopen as uReq #biblitoeka do nawiązywania połączenia ze stronką

game_url = ""

def getUrl():
	game_url=textbox.get("4.0", "end")

def findGame():
	table = []


	uClient = uReq(game_url) #nawiązujemy połączenie ze stronką pod linkiem który znajduje się w zmiennej game_url
	page_html = uClient.read() #zapisujemy do zmiennej page_html kod html tej strony do której się połączyliśmy
	uClient.close() #jak mamy juz kod html z którego korzystać będzie biblioteka bs4 to zamykamy połączenie ze stroną

	page_soup = soup(page_html, "html.parser") #parsujemy kod html do zmiennej page_soup

	game_name = page_soup.findAll("div", {"class":"apphub_AppName"}) #zapisujemy do zmiennej game_name linijke html który zawiera div z klasą "apphub_AppName"
	game_price = page_soup.findAll("div", {"class":"game_purchase_price price"}) #to samo działanie co powyżej


	for p in game_name: #ta pętla służy do wyciągnięcia z tej linijki html kawałka tekstu który nas interesuje
	     game_name = p.text

	for p in game_price:#to samo co poœyższa petla
	    game_price = p.text
	    game_price = game_price.strip() #jeżeli nawali nam niepotrzebnych spacji w stringu w którym mamy nasz tekst to używamy na nim maetody stripe() aby się ich pozbyć
	    table.append(game_price)

	print(game_name) #wypisujemy nasz tytuł
	print(table[0]) #wypisujemy cenkę tytułu

	ready = game_name + " " + table[0] #robimy stringa z wynikami naszego wyszukiwania

	txt_file = open("data.txt" , "a") #otwieramy plik data.txt z uprawnieniami read + write
	txt_file.write(ready+"\n") #zapisujemy w naszym txt stringa którego utworzylismy powyżej
	txt_file.close() #zapisujemy plik


#gui code

window = tkinter. Tk()
window.title("Games_prices")

label = Label(window, text = "Game link")
label.grid(row = 0, column = 0)

textbox = Entry(window)
textbox.grid(row = 1, column = 0, padx = 5, pady = 10)
button = Button(window, text="ADD" ,command=getUrl)
button.grid(row = 1, column  = 1)

combobox = ttk.Combobox(window, values = ["Epic Games", "Steam", "Origin", "Uplay"], state = "readonly", width = 17)
combobox.grid(row = 2, column = 0)


button1 = Button(window, text="ACCEPT" ,command=findGame)
button1.grid(row = 3, column = 0, pady = 10)

#reading games from txt.file
def readData():
	path = os.getcwd()
	parent = os.path.dirname(path)
	new = os.chdir("../webscrappers")

with open("data.txt") as f:
	label1 = Label(window, text = f.read())
	label1.grid(row = 4, column = 1)


window.geometry("400x400")
window.mainloop()

#steam webscrapper

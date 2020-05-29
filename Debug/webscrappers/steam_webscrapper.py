#biblioteki
from bs4 import BeautifulSoup as soup #biblioteka do pobierania danych ze strony
from urllib.request import urlopen as uReq #biblitoeka do nawiązywania połączenia ze stronką


game_url= input("Steam game link:") #pobieramy link do gry od użytkownika i zapisujemy w zmiennej game_url

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


print(game_name) #wypisujemy nasz tytuł
print(game_price) #wypisujemy cenkę tytułu

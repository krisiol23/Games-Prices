x = "https://store.ubi.com/eu/game?pid=591567f6ca1a6460388b4568&dwvar_591567f6ca1a6460388b4568_Platform=pcdl&edition=Standard%20Edition&source=detail"
y = "https://store.steampowered.com/app/242760/The_Forest/"

link = ["https://sasd","https://sasd1", "https://qwerty"]

skrot = ["steam","steam","ubi"]

tab = []
tab1 = []
for i in skrot:
	if(i == "steam"):
		for j in range(len(skrot)):	
			tab.append(link[j])
			break
	if(i == "ubi"):
		for n in range(len(skrot)):	
			tab1.append(link[j])
			break
			
			
print(tab)
print(tab1)


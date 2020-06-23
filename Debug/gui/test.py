x = "https://store.ubi.com/eu/game?pid=591567f6ca1a6460388b4568&dwvar_591567f6ca1a6460388b4568_Platform=pcdl&edition=Standard%20Edition&source=detail"
y = "https://store.steampowered.com/app/242760/The_Forest/"

y = y.replace("/", " ")
y = y.replace(".", " ")
y =  y.split(" ")
y = y[3]

x = x.replace("/", " ")
x = x.replace(".", " ")
x =  x.split(" ")
x = x[3]


if(x == "ubi"):
	print("cycki")

print(x)
print(y)
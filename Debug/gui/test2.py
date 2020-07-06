from tkinter import *

window = Tk()

plik = "data.txt"
j = 1
test = []
with open(plik) as f:
	cos = f.readlines()
	print(cos)

	for x in cos:
		x = x[:-1]
		test.append(x)

	print(test)

	for line in test:
		print("działa")
		label = Label(window, text = line)
		label.grid(row = j, column = 1)
		
		print(j)

		label1 = Label(window, text = "cycki")
		label1.grid(row = j, column =2)

		j+=1

window.geometry("400x400")
window.mainloop()
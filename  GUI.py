
from tkinter import *
def callback(error):
	error.destroy()
def getdata(obj, prec, img,root):
	#print( "am apasat butonul")
	error = Tk()
	error.title("EROARE")
	eroare = ""
	Ebutton = Button(error, text = eroare , command = lambda: callback(error), fg="red")
	if obj.get() ==  "":
		Ebutton.configure( text ="Nu este precizat obiectul")
		print("creez eroare")
		Ebutton.pack()
	elif img.get() == "":
		Ebutton.configure( text ="Nu este precizata imaginea")
		print("creez eroare")
		Ebutton.pack()
	else:
		try:
			val = float(prec.get())
			if val > 1: 
				raise ValueError("Am depasit Valoarea")
			if val < 0: 
				raise ValueError("Am depasit Valoarea")
			print("e ok")
			root.quit()
		except ValueError:
			Ebutton.configure( text ="Valoarea nu este corecta")
			print("creez eroare")
			Ebutton.pack()
	#error.quit()	

def GUI():
	root = Tk()
	root.title("Algortm de detectie a obiectelor")
	root.geometry("500x500")
	#Creatuin label Widget
	#Creatuin label Widget
	obj = Entry(root, width =50 )
	prec = Entry(root, width = 50 )
	img = Entry(root, width = 50 )	
	myLabelObj = Label(root, text = "Introduceti numele obiectului pe care doriti sa il cautati.")
	myLabelPrec = Label(root, text = "Introduceti precizia cu care doriti sa se decida obectul optim(0-1).")
	myLabelImg = Label(root, text = "Introduceti numele pozei pe care doriti sa o analizati.")
	OkButton = Button(root, text = "OK." , command = lambda: getdata(obj, prec, img, root) , fg="blue")
	
	#Putting it onto the screen
	myLabelObj.place(relx = 0, rely = 0.05)
	obj.place(relx = 0, rely = 0.1)
	myLabelPrec.place(relx = 0, rely = 0.25)
	prec.place(relx = 0, rely = 0.3)
	myLabelImg.place(relx = 0, rely = 0.45)
	img.place(relx = 0, rely = 0.5)
	OkButton.place(relx = 0.8, rely = 0.9)
	root.mainloop()
	object_found = obj.get()
	precision =  float(prec.get())
	pic  = img.get()
	root.destroy()
	return object_found, precision, pic


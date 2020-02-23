from tkinter import*
root = Tk()
root.title("Ask Password")

def see():
	with open('password.txt', 'r') as file:
		name = (file.readline()).strip()
		passw = (file.readline()).strip()
		if str(ent.get()) == name and str(usr_pass.get()) == passw:
			Label(root,text="Logged in !").grid(row=3,column=0)
		else:
			Label(root,text="Wrong info !").grid(row=3,column=0)

	



ask = Label(root,text="Username :")
passw = Label(root,text="Password :")
ent = Entry(root)
usr_pass = Entry(root)
enter = Button(root,text="Enter!",command=see)

ask.grid(row=0,column=0)
ent.grid(row=0,column=1)
passw.grid(row=1,column=0)
usr_pass.grid(row=1,column=1)
enter.grid(row=2,column=0,columnspan=2)

root.mainloop()
from tkinter import*
root = Tk()
root.title("Password Saver")

def save():
	real = new_inp.get()
	conf = con_inp.get()
	uname = usr_name.get()
	if str(real) == str(conf) and str(uname) != "" and str(real)!= "":
		with open("password.txt",'w') as file:
			file.write(str(uname) + "\n")
			file.write(str(real) + "\n")
		Label(root,text="Done!").grid(row=4,column=0)
	else:
		Label(root,text="Enter valid info!").grid(row=4,column=0)

name = Label(root,text="Username :")
new = Label(root,text="New Password :")
confirm = Label(root, text="Confirm Password :")
new_inp = Entry(root)
con_inp = Entry(root)
usr_name = Entry(root)
save = Button(root, text="Save!",command=save)


name.grid(row=0,column=0)
usr_name.grid(row=0,column=1)
new.grid(row=1,column=0)
confirm.grid(row=2,column=0)
new_inp.grid(row=1,column=1)
con_inp.grid(row=2,column=1)
save.grid(row=3,column=0,columnspan=2)




root.mainloop()
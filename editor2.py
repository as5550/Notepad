import tkinter
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = tkinter.Tk(className=" Text Editor")
textPad = ScrolledText(root, width=100, height=80)
text = Text(root)
text.grid()

# create a menu & define functions for each menu item
def open_command():
        file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
        if file is not None:
            contents = file.read()
            textPad.insert('1.0', contents)
            file.close()
	 
def exit_command():
    if tkinter.messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkinter.messagebox.showinfo("About", "A TextPad Designed by 'AVINASH SINGH' \n Copyright \n No rights left to reserve")
        
def new_command():
    root = tkinter.Tk(className=" Text Editor")
	# textPad = ScrolledText(root, width=100, height=80)
	
def save_command():
	global text
	t = text.get("1.0", "end-1c")
	savelocation = filedialog.asksaveasfilename()
	file1 = open(savelocation, "w+")
	file1.write(t)
	file1.close()
	
def FontHelvetica():
    global text
    text.config(font="Helvetica")
	
def FontCourier():
    global text
    text.config(font="Courier")

	
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_command)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

fontmenu = Menu(menu)
menu.add_cascade(label="Font", menu=fontmenu)
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()
fontmenu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
fontmenu.add_checkbutton(label="Helvetica", variable=Helvetica,
command=FontHelvetica) 

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

# end of menu creation
#textPad.pack()
root.mainloop()
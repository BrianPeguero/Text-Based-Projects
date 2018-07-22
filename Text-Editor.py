import Tkinter
import tkFileDialog

app = Tkinter.Tk(className="Text Editor")

#adds a textbox
text = Tkinter.Text(app)


#a dummy method
def dummy():
    print("I'm a dummy method")

#file menu commands
def openCommand():
    file = tkFileDialog.askopenfile(parent = app, mode ="rb", title="select a file")
    if file != None:
        contents = file.read()
        text.insert("1.0", contents)
        file.close()

def newCommand():
    print ("dummy")

def saveCommand():
    file = tkFileDialog.asksaveasfile(mode = "w")
    if file != None:

        file.write()
        file.close()

def exitCommand():
    app.destroy()



#creates a menu for the text editor
menu = Tkinter.Menu(app)
app.config(menu=menu)
filemenu = Tkinter.Menu(menu)

menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label="New", command = dummy())
filemenu.add_command(label="Open", command = openCommand())
filemenu.add_command(label="Save", command = saveCommand())

#____________________________________________________
filemenu.add_separator()
filemenu.add_command(label="Exit", command = exitCommand())

text.grid()
app.mainloop()
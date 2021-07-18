'''
This program will show the window of converting miles to km
and once the user enters the miles and it will return the kilometer
'''
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width =400,height=200)
window.config(padx=50,pady=30)
entry = Entry(width =10)
entry.place(x=100,y=30)

label1= Label(text="Miles")
label1.place(x=200,y=30)
label = Label(text="is equal to ")
label.place(x =20,y=65)
label3 =Label(text ="0")
label3.place(x=150,y=65)
label4=Label(text="Km")
label4.place(x=200,y=65)
def action():
    mile =float(entry.get())
    kilom =(mile) * 1.609
    label3.config(text=f"{kilom}")
button = Button(text ="Calculate",command= action)
button.place(x=120,y=100)


window.mainloop()
'''
TK inter  for GUI

'''
import tkinter

window = tkinter.Tk() # tkinter module and Tk class
window.title("Mu GUI program") # tile of the window
window.minsize(width =500, height =300) # console size
#label
my_label =tkinter.Label(text="I am a Label",font=("Arial",24,"bold")) # this line is not enough to show the label
my_label.pack() # this will plave the label into the screen and its packed in the center of the top of the window
# label can have many optional arguments 1." side = "left or right or top or bottom"
# 2. option is expand =true will take the lable in the center
# 3.**kwargs optional keyword arguments == **kw (dictionay)
#   always make a dictionary key as dict.get("something") to avoid error. dict["something"] will through error
#    if no value passed
# 4. *args - unlimited arguments but in tuples
my_label["text"] = "new text" # or
my_label.config(text="new text")

def button_clicked():
    print("I am clicked")
    my_label.config(text=input.get())

#### button
button = tkinter.Button(text="Click Me",command =button_clicked) # from tkinter import *
button.pack()


#entry

input = tkinter.Entry(width =10)
input.pack()
input.get() # returns input as string which has input from user


window.mainloop() # this mainloop will keeps the window open
'''
Password Manager application
T
'''

from tkinter import *
from tkinter import messagebox
import random
import pyperclip #Pyperclip is a cross-platform Python module for copy and paste clipboard functions.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gp_button():
    alphabets =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers =['1','2','3','4','5','6','7','8','9','0']
    symbols =['!','#','@','$','%','^','&','*','(',')','+']

    ran_a =random.sample(alphabets,6)
    ran_n=random.sample(numbers,3)
    ran_s =random.sample(symbols,3)
    ran_password= ran_a+ran_n+ran_s
    random.shuffle(ran_password)
    gp=''.join([str(x)for x in ran_password])
    pe.insert(0,gp)
    pyperclip.copy(gp)


# ---------------------------- SAVE PASSWORD ------------------------------- #
'''
this function will take all the entries that user prompted 
stores it in the file "data.txt
once the adding done and the it stored then it will show that your credentials are added
'''
def add_entries():
    w_name=website_entry.get()
    user_email= email_entry.get()
    user_password =password_entry.get()
    filename= "data.txt"
    add_done =Label(text="Your credentials added!",fg="blue") # i didnt show the message box, but you can
    '''Todo = when you add your credential, you can even show the popup window that shows that
        you have added the details with messagebox module.
        you have to import messagebox from tkinter as it is not a class
        we should add it separately.
        messagebox.showinfo(title ="title,message="added)
        messagebox.askokcancel( title,message) this line will show the details that user enteres
            and asks for ok or cancel .this method will return true or false for the ok for cancel. 
    '''
    if( len(w_name) ==0 or(len(user_password))==0 or(len (user_email))<4):
        messagebox.showinfo(title="Oops",message="You left something blank")

    else:
        is_ok = messagebox.askokcancel(title="Wedsite",message=f"{w_name}, {user_email}, "
                                                               f"{user_password}\n is it ok to save?\n")
        if(is_ok):
            with open(filename,"a") as f:
                f.write(f"{w_name}, {user_email}, {user_password}\n")
                add_done.grid(row=5,column =1)

# ---------------------------- UI SETUP ------------------------------- #
'''window setup using Tk class'''
window = Tk()
window.title("Password Manager") # title of the window
window.config(padx =20,pady=20) # padding of the window
'''Canvas for the image'''
canvas = Canvas(height =200,width =200) # canvas for the image
ph= PhotoImage(file ="logo.png") # image file - Canvas class doesn't take direct image file name
                                # need to convert into PhotoImage to include
canvas.create_image(100,95,image=ph) # creating image at the position which is center of the image
canvas.grid(row =0,column =1) # grid to show the image on the window
'''Labels for the window'''
website_label = Label(text = "Website:") # text for the website label
website_label.grid(row=1,column =0)# placing it into row 1 and column 0
email_label = Label(text= "Email/Username:")# text for the email label
email_label.grid(row=2,column =0)# placing it into row 2 and column 0
password_label =Label(text="Password:")# text for the password label
password_label.grid(row=3,column =0)# placing it into row 3 and column 0
'''Entry for he window'''
website_entry =Entry(width =35) # width of the website entry
website_entry.grid(row=1,column=1,columnspan=2)# grid placement
website_entry.focus() # focus method keeps the curser at this entry box
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2) # columnspan stretches the entry to the specified number of columns
email_entry.insert(0,"gk4045@rit.com") # this will show the initial email
pe=password_entry=Entry(width=21)
pe.grid(row=3,column=1)
'''Button for the window'''
gp_button =Button(text="Generate Password",command=gp_button)
gp_button.grid(row=3,column=2)
add_button=Button(text="Add", width =36,command=add_entries)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
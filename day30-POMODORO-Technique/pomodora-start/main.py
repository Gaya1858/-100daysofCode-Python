'''
use colorhunt.co to choose colors
'''
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps =0
timer =None

# ---------------------------- TIMER RESET ------------------------------- #
'''
once the start dutton clickes anytime the reset button can be cliked 
and when the reset button clicked, then the whole widget has to go back to initial set up 
'''
def reset_timer():
    window.after_cancel(timer)# cancel the timer that we have setup periviously
    canvas.itemconfig(timer_text,text ="00:00")
    label_heading.config(text ="Timer")
    check_marks.config(text="")
    global reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- #
'''
this function to be called when the user click the start button 
it will create work seconds,break seconds.
it will give short break when every 2 reps and long break when 8 reps completed.
based on the reps it will pass the long break, or shi=ort break or work timing to the count_down function
and change the lable according to the function
'''
def start_timer():
    global reps
    reps +=1
    work_sec =WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec =LONG_BREAK_MIN*60
    if reps % 8 ==0:
        count_down(long_break_sec)
        label_heading.config(text ="Break", fg =RED)
    elif reps % 2==0:
        count_down(short_break_sec)
        label_heading.config(text ="Break", fg =PINK)
    else:
        count_down(work_sec)
        label_heading.config(text ="Work", fg =GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
'''
this function will do the count down time for work, break .
also checks the reps and every 2 reps it will add the check mark 
'''
def count_down(count):
    count_min =math.floor(count / 60)
    count_second =count % 60
    if(count_second <=9):
        count_second =f"0{count_second}"
        '''
        a = 3
        a ="Hello" , this is called dynamic typing
        '''

    canvas.itemconfig(timer_text,text = f"{count_min}:{count_second}")
    if(count > 0):
        global timer
        timer =window.after(1000,count_down,count-1)
        # after method will wait for 1000 ms and call the function and run it once.
    else:
        start_timer()
        mark =""
        for _ in range(math.floor(reps/2)):
            mark +=cm
        check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro(Tomoto")
window.config(padx=100,pady=50,bg=YELLOW) # will change the backgroung of the window

'''
canvas widgets is like real like canvas. You cma layer widgets
'''
canvas =Canvas(width =200, height =224,bg=YELLOW,highlightthickness =0) # bg =Yellow,this background color willchange the tomoto image
# bg, but still the outline will white . we need to say highlightthickness =0 to chnage the outline hide
pi=PhotoImage(file="tomato.png") # have to create photoimage to make a canvas
canvas.create_image(100,112,image=pi)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"normal"))
cm ="✓"
canvas.grid(row=1,column =1)
label_heading =Label(text ="Timer",bg =YELLOW,fg =GREEN,font=(FONT_NAME,30,"normal"))
label_heading.grid(row=0,column =1)

button_start = Button(text="start",highlightthickness=0,command =start_timer)
button_reset =Button(text="reset",highlightthickness=0,command= reset_timer)
button_start.grid(row=2,column =0)
button_reset.grid(row =2,column=2)
check_marks =Label(fg =GREEN,bg=YELLOW)
check_marks.grid(row =3,column=1)


window.mainloop()

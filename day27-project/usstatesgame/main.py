'''
US states game: this game will show you the US mak and ask you to yype the state names. If the state name is correct
then it will place it's position.

'''
from turtle import Turtle, Screen
import pandas
from redcsv import Readcsv

FONT =("Arial",10,"normal")

'''
create_turt: creates turtle writing for each state and place it in place 
'''
def create_turt(name,pos):
    turt1 =Turtle()
    turt1.hideturtle()
    turt1.penup()
    turt1.color("black")
    turt1.goto(pos)
    turt1.write(name,align="center",font=FONT)

'''
main - will create screen and adds the shape of US map 
creates textinput icon and gets user input 
'''
screen = Screen()
turt = Turtle()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turt.shape("blank_states_img.gif")
readcsv =Readcsv()
screen.tracer(0)
count =0
game_on =True
while(game_on):
    screen.update()
    text = screen.textinput(title="State Name",prompt= "Enter another state name")

    if(text != None):
        set1 = readcsv.check_state(text)
        if(set1 != None):
            name =readcsv.get_name()
            create_turt(name,set1)
    elif (text == None):
        game_on = False
    count+=1



screen.exitonclick()
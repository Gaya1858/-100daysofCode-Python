from turtle import Turtle,Screen

# t =Turtle()
# t.shape("turtle")
# t.color("pink")
# my_screen =Screen()
#
# t.forward(100)
# t.right(90)
# my_screen.canvwidth =500
# my_screen.canvheight =500
# my_screen.exitonclick()
'''
creating table 
need to include PyPi
'''
from prettytable import PrettyTable

table =PrettyTable() # pascal case


table.add_column("Member Name",["Kanagaraj","Pushpa","Karthik","Giri","Radha","Gayathri","Balaji","Sowmiya","Bharath","Laya"])
table.add_column("Age",[72,66,63,54,48,41,26,23,23,1])
table.align ="c"

table.title="Gaya's Family Tree"

print(table)




import random
from art import logo, vs
from game_data import data

score =0
def random_people():
    people =[]
    ran1 =random.randint(0,len(data)-1)
    ran2 = random.randint(0, len(data) - 1)
    while(ran1 ==ran2):
        ran2 = random.randint(0, len(data) - 1)

    people.append(data[ran1])

    people.append(data[ran2])
    return people

def check_score(people_1,people_2):
    if(people_1["follower_count"] >people_2["follower_count"]):
        return people_1["name"]
    else:
        return people_2["name"]

def check_score1(people_1,people_2):
    if(people_1["follower_count"] >people_2["follower_count"]):
        return people_1
    else:
        return people_2

def main_all():
    print(logo)
    people = random_people( )
    dic1 = people[0]
    dic2 = people[1]
    print(print_people(dic1))
    print(vs)
    print(print_people(dic2))
    user_pick = input("Please select the person that you think higher follower: ").title( )
    result = check_score(dic1, dic2)
    global score

    if (user_pick == result):

        score += 1
        print(f"You are correct! and you score is {score}")
    else:
        print(f"You are wrong! and you score is {score}")

    print(display_winner(dic1))
    print(display_winner(dic2))
    user_choice  =input("Do you want to continue: y for yer and n for no")

    if user_choice == 'y':
        return 1
    else:
        return 0

def display_winner(win):
    return(f"name: {win['name']} and  follower_count: {win['follower_count']}")

def print_people(people):
    for i in people:
        if(i == "follower_count"):
            print("follower_count: ____ ")
        else:
            print(i,": ",people[i])


print("Welcome to Higer-Lower Game. In this game you have to choose the celebrity name who has high follower!")
replay =main_all()
while(replay ==1):
    reply =main_all()


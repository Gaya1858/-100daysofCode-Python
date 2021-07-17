'''
nameerror:  name "" is not defined , if you call the variable outside of the scope
you get nameerror

'''


#### global scope
enemies =1 # global level - available globally (for whole class) - global scope
def increse_enemies():
    global enemies
    enemies+= 2; # function variable -function level - local scope
    print("1:",enemies)

    return enemies +1
increse_enemies()
enemies =increse_enemies()
print(enemies)


enemies = ["snake","cat","dog"]
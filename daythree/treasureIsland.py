print('''   ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
''')
print(" Welcome to the Treasure Island! Your mission is to find treasure.")

way = input("You are at the cross road. do you want to move 'left' or 'right': \n")



if(way == "left"):
    swim_wait = input("do you want to swim or wait: \n")
    if(swim_wait == "wait"):
        color = input("Which color you like - yellow, red or blube: \n")
        if(color == "yellow"):
            print("Congrats you found the treasure!")
        else:
            print("You have entered to the beasts room!")
    else:
        print("You have attacked by a giant shark!")
else:
    print("You fell in the Dungen hole!")
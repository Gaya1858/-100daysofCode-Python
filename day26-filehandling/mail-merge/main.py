#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER ="[name]"
name =[]
with open("./Input/Names/invited_names.txt") as file2:
    names =file2.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt")as file1:
    content = file1.read()
    for n in names:
        sname=n.strip()
        new_letter=content.replace(PLACEHOLDER,sname)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{sname}.txt","w")as file3:
            file3.write(new_letter)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_letter =nato.to_dict()
letter_list = nato_letter["letter"].values()
code_list =nato_letter["code"].values()
newdict = {letter:code for letter in letter_list for code in code_list if(letter == code[0])}
print("Welcome to Nano Phonetic alphabet program!")
userInput = input("Enter your name: ").upper()

phonetic =[word for char in userInput for word in newdict.values() if(char ==word[0])]
print("your name phonetics are: ")
print(phonetic)
'''
Exception Handling /error handling
'''
#FileNotFoundError
#if you try read a file that doesn't exist will through error FileNotFound

#keyerror
# dict1 = {"key":"value"}
# value1=dict1["non_exist"] # there is such a key so it will through keyerror

#IndexError
# lis1=[1,2,3]
# print(lis1[3]) # we are trying to access the list index that is out of the list

#typeerror
# str1 = "boy"
# x =5
# print(str1+5) this line will thorugh typeerro because the types are different and we adding it together
'''
try: something might cause an exception

except: do this if there was an exception

else: do this if there were no exceptions

finally:do this no matter what happens

raise: raise our own exceptions
'''
# FileNotFound
# try:
#     file = open("a_file.txt")
#     keys ={"key":"value"}
#     print(keys["a"])
# except FileNotFoundError:
#     file = open("a+file.txt","w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content =file.read()
#     print(content)
# finally:# not often used but it will be very helpful.
#     raise KeyError("Just type errorthat i made up") #this eill through error
# fruits =["Apple","Pear","Orange"]
# def make_pie(index):
#     try:
#         fruit =fruits[index]
#         print(fruit+" pie")
#     except IndexError:
#         print("Fruit pie")
#
# make_pie(5)
#KeyError
fb_posts=[{'like':21,"comments":21},
          {'like':11,"comments":11,'share':23},
          {'like':31,"comments":21,'share':24},
          {'share':11,"comments":31}]

totle_likes =0

for post in fb_posts:
    try:
        totle_likes =totle_likes +post['like']
    except KeyError:
        #pass -you can even just leave pass
        totle_likes=totle_likes+0
print(totle_likes)
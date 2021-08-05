'''
there are many builtin useful functions. I have  examples for almost everything
'''
# Todo all()
lst =[1,2,3,4,5,-1,0]
# print(all(lst)) # will print false as the list containing 0. If there is a 0 then it will be false other wise
# dict1={}
# print(all(dict1))# will give true. this will be for all empty list, set, tuple and string objects
# #Todo any() like or condition. if one of the object is true in the list,dict or soon, it will return true
# #all of the objects in the list false then it will return falls
# print(any(lst)) # return true eventhough there is zero in this list
# #Todo ascii(): for ascii values of an image
# sym = "√"
# print(ascii(sym))# will return ascii value of that image of sym '\u221a'
# print("\u221a") # this will print the symbol now
# print(sym)# you can directly print the symbol too
# #Todo bin() : will return binary value of the passed value
n =12
# print(bin(n)) # returns 0b1100
#Todo callable() - you can pass in a method or function and see whetehr it is callable or not by printing without () of the
#funtion or method. returns true or falls
#Todo compile(), exce() and eval()...compile() method is used if the Python code is in string form or is an AST object,
#and you want to change it to a code object.The code object returned by compile() method can later be called
#using methods like: exec() and eval() which will execute dynamically generated Python code.
code = 'print(sum([1,2,3,4,5]))'
c =compile(code,
           'main',
           'eval')
eval(c) #return 15

#Todo getattr() and del() will get attribute from an object or a class
#Todo setattr() and del() will set an attribute from an object or a class
#Todo hasattr() and del() will check whether the object or class has that attribute
#Todo delattr() and del() will delete attribute from an object or a class
#Todo dir() will return all the directories or files
#Todo enumerate() will used to print a list as key  value pair
#you can assign a value to start a key and will increase it
new = enumerate(lst)
# print(list(new)) # will return the new list as tuples [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, -1), (6, 0)]
#for i, j in enumerate(lst,start=1):
    # print(i,':',j) # will print like key is the enumerator value from 1 and value is the value from the list
#Todo filter(): filter can be used some filtered object in
#lets filter the lst with even int
# def functions(num):
#     if(num%2==0):
#         return True
#     else:
#         return False
# even_list = list(filter(functions,lst))
# print(even_list) # returns [2, 4, 0]
#Todo help() : you can get any help using class name or method name of package name will return every details of that
#particular passed object
#help(str)# will return the below first 3 lines only
# Help on class str in module builtins:
# class str(object)
#     |  str(object='') -> str ****** there will be so many lines

#Todo id() - everything in python has an unique id number
#print(id(lst)) #returns 140647026262496
#Todo isinstance() whether an object is an instance of other class or not.
#this method will work in builtin and custom designed classes.

# print(isinstance(n,int))# n=12, returns true as n is an integer value
# print(isinstance(n,float))# returns false as n is not a float value
#Todo iter() and next(): these two method be used togetehr to remove a item from a created iter().
#lite =iter(lst)#[1,2, 3, 4, 5, -1, 0]
# print(next(lite)) # returns the first element in the list which is 1 and removed it from the lite
# #print([x for x in lite])# [2, 3, 4, 5, -1, 0]
# print(next(lite)) # returns the first element in the list which is 2 now and removed it from the lite
# print([x for x in lite])#[3, 4, 5, -1, 0]
# Todo Locals()
# def functions(num):
#     if(num%2==0):
#         print(locals())# this will prints the local variable and its value
#         # {'num': 2}
#         # {'num': 4}
#         # {'num': 0}
#         return True
#
#     else:
#         return False
# lite=map(functions,lst)
# print(list(lite))#[False, True, False, True, False, False, True]
#Todo print(): there are many ways to use this print function to display the materials
# print(1,2,3) # output -1 2 3
# print(1,2,3,sep= '**')# output 1**2**3. you can add any symbol to seperate the elements
# print(1,file="new.txt") # there is no file new.txt exist but you can write on a file like this too
#Todo *********** format() : there are many useful ways to format the output using format method
print(format(12,'d'))# decimal int
print(format(12,'b'))# binary number
print(format(12,'x'))# hexa decimal number
print(format(12,'o'))# octa decimal number
print(format(12.23567788,'f'))# first 6decimal point numbers 12.235678. if you want specified decimal point then
#use '.nf' , n is number of decial points you want. if you want juest 2 then .2f
print(format(12,'%'))# return the percentage of the number 1200.000000%
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
print(format("age",'>10')) #        age

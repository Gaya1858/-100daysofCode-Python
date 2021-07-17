# function that take unlimited arguments
# * takes all of the arguments as tuple
def add(*gaya):
    sum1 =0
    for i in gaya:
       sum1 +=i
    return sum1

# **kwargs === keyword arguments ---- unlimited keyword argument
# many keyward arguments
def calculate(**kwargs): # kwargs values will be stored as dictionary
    print(kwargs)
    #{'add': 3, 'multiply': 5}

print(add(1,2,3,4,5,6,7))
calculate(add=3,multiply =5)
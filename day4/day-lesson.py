# random number generation
# but computers perfron predictable way. Whole bunch ones and zeros used to create random number
# the mathe this is used in random number generation is Marsenne Twister algorithm
# check sudo random number generation
'''
    Python random Module

'''
import random # random module


random_int = random.randint(1,10) # specifing any integer from 1 to 10 [1,10]
print(random_int)


# generating random float
random_float = random.random() # will return 0.0 to 1.0 not including one [0,1]
print(random_float)

# what if i want random float from 1 to 5
#we can mulptifly with the number like random_float *5

print(random_float*5)


